# Hackathon Tasks

Objective: Build a website where people can find local doctors who are accepting new patients and can speak the user's language.
Time Budget (hours): 11.07

## Top Features
- [ ] Server-side filtering for 'accepting new patients' status
- [ ] Location-based search using city/region input
- [ ] Multi-criteria filtering (language + location + acceptance status)
- [ ] Frontend search form with checkboxes and input fields
- [ ] Fix PATCH route for updating acceptance status

## 24-Hour Plan
- [ ] Backend Fixes (2 hours)
  - Fixed PATCH route for accepting_patients field
  - Server-side filtering for location and acceptance status
  - API endpoints tested with Postman
- [ ] Frontend Integration (4 hours)
  - Search form with location input, acceptance status checkbox, language dropdown
  - Modified API calls to send all filters
  - Removed client-side filtering
- [ ] Data & Testing (2 hours)
  - Seed database with sample doctors
  - Tested multi-criteria filtering
  - Basic location input validation
- [ ] Polish & Demo (3 hours)
  - Responsive UI design
  - Demo script preparation
  - Final bug fixes

## Judge Snapshot (1-10)
- Topic Alignment: 3
- Innovation: 3
- Solution Effectiveness: 2
- Technical Challenge: 5
- UI/Design Effort: 4
- Overall Score: 3

## Judging Summary
- Project has a solid technical foundation but fails to implement core functionality required for its objective. Critical gaps in acceptance status filtering, location-based search, and authentication prevent the solution from being functional. While the architecture is sound, the current state lacks essential features needed for a viable healthcare search tool, making it a high-risk demo with significant work remaining.

## Defer / Not Now
- [ ] User authentication for admin operations
- [ ] Distance-based geolocation search
- [ ] Admin interface for managing doctors
- [ ] Language code validation
- [ ] Client-side filtering for performance

## Review Notes
- No major issues flagged by ReviewerAgent.
