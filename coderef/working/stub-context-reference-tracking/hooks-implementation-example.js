/**
 * Hooks System Implementation Example
 *
 * This is a reference implementation showing how to build the hooks system
 * for the coderef orchestrator. Based on everything-claude-code patterns.
 *
 * @author CodeRef Assistant
 * @date 2026-01-19
 * @related stub-context-reference-tracking
 */

const chokidar = require('chokidar');
const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');
const { execSync } = require('child_process');

// ============================================================================
// Configuration Loader
// ============================================================================

class HooksConfig {
  constructor(configPath = '.claude/hooks.yaml') {
    this.configPath = configPath;
    this.hooks = [];
    this.load();
  }

  load() {
    try {
      const content = fs.readFileSync(this.configPath, 'utf8');
      const config = yaml.load(content);
      this.hooks = config.hooks || [];
      console.log(`[Hooks] Loaded ${this.hooks.length} hooks from ${this.configPath}`);
    } catch (error) {
      console.error(`[Hooks] Failed to load config: ${error.message}`);
      this.hooks = [];
    }
  }

  reload() {
    console.log('[Hooks] Reloading configuration...');
    this.load();
  }
}

// ============================================================================
// Condition Evaluator
// ============================================================================

class ConditionEvaluator {
  /**
   * Evaluate a condition string with context
   * @param {string} condition - Condition expression (e.g., "status == 'complete'")
   * @param {object} context - Context variables
   * @returns {boolean}
   */
  static evaluate(condition, context) {
    if (!condition) return true;

    try {
      // Create safe evaluation context
      const safeContext = {
        json: context.json || {},
        file_path: context.file_path || '',
        workorder_id: context.workorder_id || null,
        ...context
      };

      // Simple condition parser (production would use proper parser)
      // Supports: json.field == "value", field != null, etc.
      const func = new Function(...Object.keys(safeContext), `return ${condition}`);
      return func(...Object.values(safeContext));
    } catch (error) {
      console.error(`[Hooks] Condition evaluation failed: ${condition}`, error);
      return false;
    }
  }
}

// ============================================================================
// Action Executor
// ============================================================================

class ActionExecutor {
  /**
   * Execute a hook action
   * @param {string} action - Action to execute (MCP tool or shell command)
   * @param {object} params - Parameters for the action
   * @param {object} context - Execution context
   */
  static async execute(action, params, context) {
    console.log(`[Hooks] Executing action: ${action}`);

    // MCP Tool Actions
    if (action.startsWith('mcp__')) {
      return await this.executeMcpTool(action, params, context);
    }

    // Shell Commands
    if (action.startsWith('bash:')) {
      const command = action.replace('bash:', '');
      return await this.executeShellCommand(command, params, context);
    }

    // Custom Actions
    if (action.startsWith('custom:')) {
      const customAction = action.replace('custom:', '');
      return await this.executeCustomAction(customAction, params, context);
    }

    throw new Error(`Unknown action type: ${action}`);
  }

  static async executeMcpTool(tool, params, context) {
    // Replace template variables in params
    const resolvedParams = this.resolveParams(params, context);

    console.log(`[Hooks] MCP Tool: ${tool}`, resolvedParams);

    // In production, this would call the actual MCP server
    // For now, simulate with shell command
    const mcpCommand = this.buildMcpCommand(tool, resolvedParams);

    try {
      const result = execSync(mcpCommand, { encoding: 'utf8' });
      console.log(`[Hooks] MCP Tool result:`, result);
      return { success: true, result };
    } catch (error) {
      console.error(`[Hooks] MCP Tool failed:`, error.message);
      return { success: false, error: error.message };
    }
  }

  static async executeShellCommand(command, params, context) {
    const resolvedCommand = this.resolveTemplate(command, context);
    console.log(`[Hooks] Shell: ${resolvedCommand}`);

    try {
      const result = execSync(resolvedCommand, { encoding: 'utf8' });
      console.log(`[Hooks] Shell result:`, result);
      return { success: true, result };
    } catch (error) {
      console.error(`[Hooks] Shell failed:`, error.message);
      return { success: false, error: error.message };
    }
  }

  static async executeCustomAction(actionName, params, context) {
    // Custom actions for specific workflows
    const actions = {
      verify_workorder_completion: this.verifyWorkorderCompletion,
      regenerate_dashboard: this.regenerateDashboard,
      update_projects_md: this.updateProjectsMd,
    };

    const action = actions[actionName];
    if (!action) {
      throw new Error(`Unknown custom action: ${actionName}`);
    }

    return await action.call(this, params, context);
  }

  // ========================================================================
  // Custom Action Implementations
  // ========================================================================

  static async verifyWorkorderCompletion(params, context) {
    console.log(`[Hooks] Verifying workorder completion:`, params.workorder_id);

    // Read communication.json
    const commPath = path.join(context.project_path, 'communication.json');
    const communication = JSON.parse(fs.readFileSync(commPath, 'utf8'));

    // Verify status
    if (communication.status !== 'complete') {
      return { success: false, error: 'Status is not complete' };
    }

    // Verify archived
    if (!communication.handoff.archived) {
      return { success: false, error: 'Feature not archived' };
    }

    // Verify DELIVERABLES.md
    const deliverablesPath = path.join(context.project_path, 'DELIVERABLES.md');
    if (!fs.existsSync(deliverablesPath)) {
      return { success: false, error: 'DELIVERABLES.md not found' };
    }

    const deliverables = fs.readFileSync(deliverablesPath, 'utf8');
    if (deliverables.includes('TBD')) {
      return { success: false, error: 'DELIVERABLES.md contains TBD values' };
    }

    // Update communication.json status to verified
    communication.status = 'verified';
    fs.writeFileSync(commPath, JSON.stringify(communication, null, 2));

    // Update workorders.json
    const workordersPath = 'C:\\Users\\willh\\Desktop\\assistant\\workorders.json';
    const workorders = JSON.parse(fs.readFileSync(workordersPath, 'utf8'));

    const workorder = workorders.active_workorders.find(
      w => w.workorder_id === params.workorder_id
    );

    if (workorder) {
      workorder.status = 'verified';
      workorder.verified_at = new Date().toISOString();
      fs.writeFileSync(workordersPath, JSON.stringify(workorders, null, 2));
    }

    console.log(`[Hooks] Workorder ${params.workorder_id} verified successfully`);
    return { success: true, workorder_id: params.workorder_id };
  }

  static async regenerateDashboard(params, context) {
    console.log(`[Hooks] Regenerating dashboard...`);

    // In production, this would trigger dashboard rebuild
    // For now, just log
    return { success: true, message: 'Dashboard regenerated' };
  }

  static async updateProjectsMd(params, context) {
    console.log(`[Hooks] Updating projects.md...`);

    // In production, this would update projects.md
    return { success: true, message: 'projects.md updated' };
  }

  // ========================================================================
  // Utility Methods
  // ========================================================================

  static resolveParams(params, context) {
    const resolved = {};
    for (const [key, value] of Object.entries(params)) {
      if (typeof value === 'string') {
        resolved[key] = this.resolveTemplate(value, context);
      } else {
        resolved[key] = value;
      }
    }
    return resolved;
  }

  static resolveTemplate(template, context) {
    return template.replace(/\$\{([^}]+)\}/g, (match, variable) => {
      // Support nested properties (e.g., ${json.workorder_id})
      const value = variable.split('.').reduce((obj, key) => obj?.[key], context);
      return value !== undefined ? value : match;
    });
  }

  static buildMcpCommand(tool, params) {
    // Build command to invoke MCP tool
    // In production, this would use proper MCP client
    const paramsJson = JSON.stringify(params);
    return `echo "MCP: ${tool} with params: ${paramsJson}"`;
  }
}

// ============================================================================
// Hook Matcher
// ============================================================================

class HookMatcher {
  /**
   * Check if a file path matches a trigger pattern
   * @param {string} pattern - Trigger pattern (e.g., "write:coderef/working/* /stub.json")
   * @param {string} filePath - File path that changed
   * @param {string} event - Event type (add, change, unlink)
   * @returns {boolean}
   */
  static matches(pattern, filePath, event) {
    // Parse pattern: "operation:glob-pattern"
    const [operation, globPattern] = pattern.split(':');

    // Map file watcher events to operations
    const eventMap = {
      add: 'write',
      change: 'edit',
      unlink: 'delete'
    };

    const mappedOperation = eventMap[event];
    if (operation !== mappedOperation) {
      return false;
    }

    // Match glob pattern
    return this.matchGlob(globPattern, filePath);
  }

  static matchGlob(pattern, filePath) {
    // Simple glob matcher (production would use minimatch or similar)
    // Supports: *, **, ?
    const regex = pattern
      .replace(/\*/g, '[^/\\\\]*')
      .replace(/\*\*/g, '.*')
      .replace(/\?/g, '.');

    return new RegExp(`^${regex}$`).test(filePath);
  }
}

// ============================================================================
// Hooks Engine
// ============================================================================

class HooksEngine {
  constructor(configPath) {
    this.config = new HooksConfig(configPath);
    this.watcher = null;
    this.executionLog = [];
  }

  start(watchPath = 'C:\\Users\\willh\\Desktop\\assistant') {
    console.log(`[Hooks] Starting hooks engine...`);
    console.log(`[Hooks] Watching: ${watchPath}`);

    this.watcher = chokidar.watch(watchPath, {
      ignored: /(^|[\/\\])\../, // Ignore dotfiles
      persistent: true,
      ignoreInitial: true,
      awaitWriteFinish: {
        stabilityThreshold: 500,
        pollInterval: 100
      }
    });

    // Watch for file changes
    this.watcher
      .on('add', path => this.handleFileEvent('add', path))
      .on('change', path => this.handleFileEvent('change', path))
      .on('unlink', path => this.handleFileEvent('unlink', path));

    // Watch for config changes
    this.watcher.on('change', path => {
      if (path.endsWith('hooks.yaml')) {
        this.config.reload();
      }
    });

    console.log(`[Hooks] Engine started with ${this.config.hooks.length} hooks`);
  }

  stop() {
    if (this.watcher) {
      this.watcher.close();
      console.log('[Hooks] Engine stopped');
    }
  }

  async handleFileEvent(event, filePath) {
    console.log(`[Hooks] File ${event}: ${filePath}`);

    // Find matching hooks
    const matchingHooks = this.config.hooks.filter(hook =>
      HookMatcher.matches(hook.trigger, filePath, event)
    );

    if (matchingHooks.length === 0) {
      return;
    }

    console.log(`[Hooks] Found ${matchingHooks.length} matching hooks`);

    // Build context
    const context = await this.buildContext(filePath, event);

    // Execute hooks
    for (const hook of matchingHooks) {
      await this.executeHook(hook, context);
    }
  }

  async buildContext(filePath, event) {
    const context = {
      file_path: filePath,
      event: event,
      timestamp: new Date().toISOString()
    };

    // If JSON file, parse and add to context
    if (filePath.endsWith('.json')) {
      try {
        const content = fs.readFileSync(filePath, 'utf8');
        context.json = JSON.parse(content);
        context.workorder_id = context.json.workorder_id || null;
      } catch (error) {
        console.error(`[Hooks] Failed to parse JSON: ${error.message}`);
      }
    }

    // Extract project path
    const match = filePath.match(/coderef[\/\\]working[\/\\]([^\/\\]+)/);
    if (match) {
      context.feature_name = match[1];
      context.project_path = path.dirname(filePath);
    }

    return context;
  }

  async executeHook(hook, context) {
    console.log(`[Hooks] Executing hook: ${hook.name}`);

    // Check condition
    if (hook.condition) {
      const conditionMet = ConditionEvaluator.evaluate(hook.condition, context);
      if (!conditionMet) {
        console.log(`[Hooks] Condition not met, skipping: ${hook.condition}`);
        return;
      }
    }

    // Apply debounce if configured
    if (hook.debounce) {
      await this.debounce(hook.name, hook.debounce);
    }

    // Execute action
    try {
      const result = await ActionExecutor.execute(hook.action, hook.params || {}, context);

      // Log execution
      this.executionLog.push({
        hook: hook.name,
        timestamp: new Date().toISOString(),
        context: context,
        result: result,
        success: result.success
      });

      // Log message
      if (hook.log) {
        const logMessage = ActionExecutor.resolveTemplate(hook.log, context);
        console.log(`[Hooks] ${logMessage}`);
      }

      console.log(`[Hooks] Hook executed successfully: ${hook.name}`);
    } catch (error) {
      console.error(`[Hooks] Hook execution failed: ${hook.name}`, error);
      this.executionLog.push({
        hook: hook.name,
        timestamp: new Date().toISOString(),
        context: context,
        error: error.message,
        success: false
      });
    }
  }

  async debounce(hookName, milliseconds) {
    // Simple debounce implementation
    const now = Date.now();
    const lastExecution = this.executionLog
      .filter(log => log.hook === hookName)
      .pop();

    if (lastExecution) {
      const timeSinceLastExecution = now - new Date(lastExecution.timestamp).getTime();
      if (timeSinceLastExecution < milliseconds) {
        const waitTime = milliseconds - timeSinceLastExecution;
        console.log(`[Hooks] Debouncing ${hookName} for ${waitTime}ms`);
        await new Promise(resolve => setTimeout(resolve, waitTime));
      }
    }
  }

  getExecutionLog() {
    return this.executionLog;
  }
}

// ============================================================================
// Example Usage
// ============================================================================

if (require.main === module) {
  // Create hooks engine
  const engine = new HooksEngine('.claude/hooks.yaml');

  // Start watching
  engine.start('C:\\Users\\willh\\Desktop\\assistant');

  // Log execution summary every 30 seconds
  setInterval(() => {
    const log = engine.getExecutionLog();
    const recent = log.slice(-10);
    console.log('\n=== Recent Hook Executions ===');
    recent.forEach(entry => {
      const status = entry.success ? '✓' : '✗';
      console.log(`${status} ${entry.hook} - ${entry.timestamp}`);
    });
    console.log('==============================\n');
  }, 30000);

  // Graceful shutdown
  process.on('SIGINT', () => {
    console.log('\n[Hooks] Shutting down...');
    engine.stop();
    process.exit(0);
  });

  console.log('[Hooks] Press Ctrl+C to stop');
}

module.exports = { HooksEngine, HooksConfig, ActionExecutor, ConditionEvaluator, HookMatcher };
