# Jovi's Home & Salon Organizer - Features Documentation

**Project:** Gamified ADHD-Friendly Task Management App
**User:** Jovi
**Created:** 2025-12-30
**Version:** 1.0.0
**Stub ID:** STUB-064

---

## Table of Contents

1. [Overview](#overview)
2. [Core Features](#core-features)
   - [Three Main Categories](#three-main-categories)
   - [Bottom Tab Navigation](#bottom-tab-navigation)
   - [Task Breakdown System](#task-breakdown-system)
   - [Weekly Calendar Widget](#weekly-calendar-widget)
3. [ADHD-Friendly Tools](#adhd-friendly-tools)
   - [Visual Countdown Timers](#visual-countdown-timers)
   - [Color-Coded Priority System](#color-coded-priority-system)
   - [Focus Mode](#focus-mode)
   - [Task Notes Feature](#task-notes-feature)
   - [Pause/Resume Functionality](#pauseresume-functionality)
   - [Sound Effects](#sound-effects-optional)
   - [Daily Reminders](#daily-reminders)
   - [Flexible View Switching](#flexible-view-switching)
4. [Gamification Elements](#gamification-elements)
   - [Points System](#points-system)
   - [Experience and Levels](#experience-xp-and-levels)
   - [Streak Tracking](#streak-tracking)
   - [Achievement Badges](#achievement-badges)
   - [Reward Popups](#reward-popups)
5. [Task Examples by Category](#task-examples-by-category)
   - [Home Tasks](#home-tasks)
   - [Shop Tasks (Salon)](#shop-tasks-salon)
   - [Life Tasks (Personal)](#life-tasks-personal)
6. [Design Specifications](#design-specifications)
   - [Color Palette](#color-palette)
   - [Typography](#typography)
   - [Layout](#layout)
   - [Responsive Breakpoints](#responsive-breakpoints)
7. [Technical Implementation](#technical-implementation)
   - [Architecture](#architecture)
   - [Key Technologies](#key-technologies)
   - [State Management](#state-management)
   - [Event Handling](#event-handling)
8. [User Workflows](#user-workflows)
   - [Completing a Task](#completing-a-task)
   - [Using Focus Mode](#using-focus-mode)
   - [Tracking Streaks](#tracking-streaks)
   - [Unlocking Achievements](#unlocking-achievements)
9. [Future Enhancements](#future-enhancements-not-yet-implemented)
10. [Credits](#credits)

---

## Overview

A comprehensive task management application designed specifically for ADHD users to manage household cleaning, laundry, decluttering, and salon care tasks with gamification, visual aids, and focus-enhancing tools.

**Design Theme:** Rose gold, black, and purple with warm golden accents
**Platform:** Mobile-responsive web application
**Architecture:** Single-file HTML with embedded CSS and JavaScript

---

## Core Features

### Three Main Categories

- **Home:** Cleaning, laundry, and decluttering tasks
- **Shop:** Salon management (tool sanitization, restocking, client prep)
- **Life:** Personal wellness (self-care, meal prep, exercise, budgeting)

### Bottom Tab Navigation

- Fixed bottom navigation bar
- Three main tabs: Home | Shop | Life
- Mobile-friendly with safe-area-inset support for notched devices
- Icon-based navigation

### Task Breakdown System

- Each task divided into manageable steps
- Expandable step-by-step instructions
- Progress tracking per task (e.g., "0/5 steps completed")
- Visual progress bars

### Weekly Calendar Widget

- Current week view
- Streak indicators with fire emoji (🔥)
- Visual feedback for consecutive completion days
- Highlights current day

---

## ADHD-Friendly Tools

### Visual Countdown Timers

- Individual timer for each task
- Default durations based on task complexity
- Display format: MM:SS (e.g., 45:00)
- Start/Pause/Resume controls
- Automatic completion notifications
- Audio cue when timer completes

**Implementation:**
```javascript
// Timer system with pause/resume
const timerId = setInterval(() => {
    timeLeft--;
    timerDisplay.textContent = `${minutes}:${seconds}`;
    if (timeLeft <= 0) {
        playSound('complete');
        showNotification('⏰ Time\'s Up!');
    }
}, 1000);
```

### Color-Coded Priority System

Visual priority badges on each task card:

| Priority | Color | Hex Code |
|----------|-------|----------|
| High | Red | #FF6B6B |
| Medium | Yellow | #FFD93D |
| Low | Green | #6BCF7F |

### Focus Mode

- Toggle button (🎯) in header
- Dims non-active tasks to 30% opacity
- Disables interaction with inactive tasks
- Automatically activates when timer starts
- Reduces visual distractions and cognitive load

**CSS Implementation:**
```css
body.focus-mode .task-card:not(.active-task) {
    opacity: 0.3;
    pointer-events: none;
}
```

### Task Notes Feature

- Expandable note-taking area for each task
- Save personal reminders or modifications
- Accessible via 📝 Notes button
- Persistent across sessions (when backend added)

### Pause/Resume Functionality

- All timers support pause and resume
- Maintains time remaining when paused
- Visual feedback (button state changes)
- Prevents loss of progress during interruptions

### Sound Effects (Optional)

- Toggle button (🔊/🔇) in header
- Completion sound (800Hz tone)
- Tick sound for timer countdown (600Hz tone)
- Generated using Web Audio API
- Can be disabled for quiet environments

### Daily Reminders

- Toggle button (🔔) in header
- Browser notification permission request
- Customizable reminder times
- Popup notifications for task reminders

### Flexible View Switching

- Daily, Weekly, and Monthly view buttons
- Adaptable scheduling based on user needs
- Visual indicator for active view
- Helps with different planning preferences

---

## Gamification Elements

### Points System

- Each task awards points based on complexity
- Example: Quick tasks = 20 pts, Deep cleaning = 100 pts
- Points accumulate toward leveling up
- Displayed in stats bar at top

### Experience (XP) and Levels

- XP bar with visual progress indicator
- Level progression system
- Current implementation shows Level 5 (example)
- Motivates continued engagement

### Streak Tracking

- Consecutive days of task completion
- Fire emoji indicators on calendar (🔥)
- Example: 7-day streak displayed
- Encourages daily consistency

### Achievement Badges

Six unlockable achievement types:

| Badge | Icon | Requirement |
|-------|------|-------------|
| First Task | 🎯 | Complete your first task |
| 7-Day Streak | 🔥 | Maintain streak for 7 days |
| 30 Tasks | ⭐ | Complete 30 total tasks |
| Deep Clean | 💪 | Finish a major cleaning task |
| Level 10 | 🏆 | Reach level 10 |
| Salon Pro | 👑 | Complete 20 salon tasks |

Features:
- Visual unlock animations
- Grayscale when locked, full color when unlocked
- Bounce animation on achievement unlock

### Reward Popups

- Appear on task completion
- Show points earned
- Celebratory visual feedback
- Auto-dismiss after brief display

---

## Task Examples by Category

### Home Tasks

| Task | Points | Priority | Duration | Steps |
|------|--------|----------|----------|-------|
| Kitchen Deep Clean | 50 | High | 45 min | Clear counters, wipe surfaces, clean appliances, mop floor, organize |
| Bathroom Refresh | 30 | Medium | 30 min | Scrub toilet, clean sink, wipe mirrors, mop floor, restock supplies |
| Living Room Tidy | 20 | Low | 20 min | Pick up items, vacuum, dust surfaces, arrange pillows, declutter |
| Weekly Laundry | 40 | Medium | 60 min | Sort clothes, wash loads, dry, fold, put away |
| Bedroom Reset | 30 | Medium | 25 min | Make bed, organize nightstand, vacuum, dust, clear surfaces |
| Declutter Closet | 60 | High | 90 min | Remove items, sort keep/donate, organize by category, vacuum, rearrange |

### Shop Tasks (Salon)

| Task | Points | Priority | Duration | Steps |
|------|--------|----------|----------|-------|
| Sanitize Tools | 40 | High | 30 min | Gather tools, wash with soap, disinfect, dry, organize storage |
| Restock Supplies | 30 | Medium | 20 min | Check inventory, make list, order items, organize stock, update log |
| Client Area Prep | 25 | Medium | 15 min | Clean stations, arrange tools, check lighting, prep products, sanitize chairs |

### Life Tasks (Personal)

| Task | Points | Priority | Duration | Steps |
|------|--------|----------|----------|-------|
| Morning Self-Care | 20 | High | 20 min | Skincare routine, brush teeth, style hair, moisturize, prepare for day |
| Meal Prep Sunday | 50 | Medium | 90 min | Plan meals, grocery shop, prep ingredients, cook batches, store portions |
| Weekly Exercise | 40 | High | 45 min | Warm up, cardio session, strength training, cool down, stretch |
| Budget Check | 30 | Medium | 30 min | Review expenses, categorize spending, check savings, plan week, adjust goals |

---

## Design Specifications

### Color Palette

```css
--primary-gold: #D4AF37;      /* Warm golden */
--rose-gold: #B87E7E;         /* Accent */
--dark-bg: #1a1a1a;           /* Main background */
--card-bg: #2a2a2a;           /* Task cards */
--purple-accent: #9B6B9E;     /* Highlights */
--text-color: #f0f0f0;        /* Primary text */
--priority-high: #FF6B6B;     /* High priority badge */
--priority-medium: #FFD93D;   /* Medium priority badge */
--priority-low: #6BCF7F;      /* Low priority badge */
```

### Typography

- **Headers:** 'Playfair Display', serif
- **Body:** 'Cormorant Garamond', serif
- **Timers/Numbers:** monospace

### Layout

- 2-column grid on desktop (min-width: 768px)
- 1-column grid on mobile
- Fixed header with stats and controls
- Fixed bottom navigation
- Scrollable content area
- Card-based task design with rounded corners

### Responsive Breakpoints

| Breakpoint | Width | Layout |
|------------|-------|--------|
| Mobile | < 768px | 1-column grid |
| Desktop | ≥ 768px | 2-column grid |

---

## Technical Implementation

### Architecture

- Single HTML file (`index.html`)
- Embedded CSS (no external stylesheets)
- Embedded JavaScript (no external dependencies)
- Google Fonts: Playfair Display, Cormorant Garamond

### Key Technologies

| Technology | Purpose |
|------------|---------|
| Web Audio API | Sound effect generation |
| CSS Grid | Responsive layout |
| CSS Flexbox | Component alignment |
| CSS Animations | Visual feedback and transitions |
| JavaScript Map() | Timer state management |
| DOM Manipulation | Dynamic updates |
| Notification API | Daily reminders |

### State Management

```javascript
// Active timers tracked in Map object
const activeTimers = new Map();

// Toggle states
let focusModeEnabled = false;
let soundEnabled = true;
let reminderEnabled = false;

// View mode
let currentView = 'daily'; // 'daily' | 'weekly' | 'monthly'
```

### Event Handling

- Click events for buttons and toggles
- Timer start/pause/resume logic
- Step completion tracking
- Task expansion/collapse
- Notes textarea management

---

## User Workflows

### Completing a Task

1. Select task category (Home/Shop/Life)
2. Review task card and priority level
3. Click **"📋 Steps"** to view breakdown
4. Click **"▶ Start"** to begin timer
5. Focus mode automatically activates
6. Complete each step, checking off as you go
7. Add notes if needed via **"📝 Notes"**
8. Timer completes, plays sound
9. Reward popup appears showing points earned
10. Task marked complete, progress updated

### Using Focus Mode

1. Click **🎯** button in header (or automatic on timer start)
2. All inactive tasks dim to 30% opacity
3. Only active task remains fully visible
4. Interaction disabled for dimmed tasks
5. Click **🎯** again to exit focus mode

### Tracking Streaks

1. Complete at least one task daily
2. Check calendar widget for fire emojis (🔥)
3. Consecutive days build streak count
4. Unlock 7-Day Streak achievement badge
5. Maintain consistency for higher streaks

### Unlocking Achievements

1. Complete milestone requirements
2. Badge icon changes from grayscale to color
3. Bounce animation plays
4. Achievement displayed in banner
5. Notification popup confirms unlock

---

## Future Enhancements (Not Yet Implemented)

Potential additions for full application:

- [ ] Backend database for data persistence
- [ ] User authentication and profiles
- [ ] Custom task creation interface
- [ ] Task scheduling and recurring tasks
- [ ] Analytics dashboard with charts
- [ ] Multi-user household sharing
- [ ] Mobile app versions (iOS/Android)
- [ ] Push notifications via service worker
- [ ] Dark/light theme toggle
- [ ] Custom color scheme editor
- [ ] Export/import task data
- [ ] Integration with calendar apps
- [ ] Voice command support
- [ ] Habit tracking extensions

---

## Credits

**Developed for:** Jovi
**Project ID:** STUB-064 (CodeRef Orchestrator)
**Status:** Planning/Mockup Phase
**Target:** New standalone application

**Research informed by ADHD-friendly cleaning strategies from:**
- Sweepy app
- Tiimo planner
- Inflow ADHD app
- Chore Focus
- ADHD cleaning methodology best practices

---

**Last Updated:** 2025-12-30
**Documentation Version:** 1.0.0
