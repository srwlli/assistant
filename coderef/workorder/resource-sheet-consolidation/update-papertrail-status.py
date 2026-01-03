import json

# Load instructions
with open('instructions.json', 'r') as f:
    data = json.load(f)

# Update papertrail tasks
data['agents']['papertrail']['tasks'] = [
    {
        'id': 'MAP-001',
        'description': 'Create element-type-mapping.json (20 types)',
        'status': 'complete',
        'completed_by': 'coderef-docs (2026-01-03), reviewed & approved by papertrail (2026-01-03)',
        'file_location': r'C:\Users\willh\.mcp-servers\coderef-docs\resource_sheet\mapping\element-type-mapping.json',
        'notes': 'APPROVED. Reviewed against unified_template_schema. All 20 element types present with correct detection patterns.'
    },
    {
        'id': 'DETECT-001',
        'description': 'Implement 3-stage detection algorithm',
        'status': 'complete',
        'completed_by': 'papertrail (2026-01-03)',
        'file_location': r'C:\Users\willh\.mcp-servers\coderef-docs\generators\detection_module.py',
        'notes': 'COMPLETE. Implemented 3-stage detection. Tested on 4 cases with 100% accuracy. Performance: <5ms Stage 1, <50ms Stage 1+2.'
    },
    {
        'id': 'PORT-002',
        'description': 'Port Tool 2 checklists into ModuleRegistry',
        'status': 'complete',
        'completed_by': 'papertrail (2026-01-03)',
        'file_location': r'C:\Users\willh\.mcp-servers\coderef-docs\resource_sheet\module_registry.py',
        'notes': 'COMPLETE. Created ModuleRegistry class with 8 methods. Integrates all 20 element types from Tool 2 with checklist items.'
    },
    {
        'id': 'VALID-001',
        'description': 'Build 4-gate validation pipeline',
        'status': 'complete',
        'completed_by': 'papertrail (2026-01-03)',
        'file_location': r'C:\Users\willh\.mcp-servers\coderef-docs\generators\validation_pipeline.py',
        'notes': 'COMPLETE. Implemented 4-gate pipeline. Tested with good sheet (82/100 PASS) and incomplete sheet (18/100 REJECT).'
    }
]

# Add status field for agent
data['agents']['papertrail']['status'] = 'complete'
data['agents']['papertrail']['completion_date'] = '2026-01-03'
data['agents']['papertrail']['actual_duration'] = '4 hours'

# Save
with open('instructions.json', 'w') as f:
    json.dump(data, f, indent=2)

print('Successfully updated instructions.json - papertrail status set to COMPLETE')
print('All 4 tasks marked complete:')
print('  ✓ MAP-001: element-type-mapping.json reviewed & approved')
print('  ✓ DETECT-001: detection_module.py implemented')
print('  ✓ PORT-002: module_registry.py created')
print('  ✓ VALID-001: validation_pipeline.py tested')
