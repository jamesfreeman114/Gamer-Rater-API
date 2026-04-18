<!-- Last updated: 2026-04-18 -->
<!-- Last change: One rating per player per game; can be updated -->

# GamerRater - Product Requirements Document

## Problem Statement

A local startup has received seed funding to build a platform where gamers can discover, discuss, and rate the games they play. The platform needs a reliable backend API that stores game information, supports user-submitted content (reviews, ratings, images), and enables searching and filtering by category and release year.

## Target Users

Players (gamers) who want to:
- Log games they have played
- Share opinions through ratings and written reviews
- Discover games by browsing, searching, and filtering

## Core Requirements

- Players can create new game entries; no two players can create a duplicate game in the system
- Players can upload pictures for a game
- Players can rate a game (numeric score)
- Players can write a text review for a game
- Games expose an average rating, calculated as a custom model property (not stored in the database)
- Games can be searched by name
- Games can be filtered/sorted by category
- Games can be filtered/sorted by year of release

## Technical Stack

### Stack Decisions

| Tool | Choice | Rationale |
|------|--------|-----------|
| Language | Python 3.12 | Required by the project environment |
| Web framework | Django | Provides ORM, admin, and project structure out of the box |
| API layer | Django REST Framework | Standard choice for building REST APIs on top of Django |
| Database | SQLite | Sufficient for a portfolio project; no external database server needed |
| CORS | django-cors-headers | Allows a future frontend to connect to the API |
| Package management | Pipenv | Already configured in the project |

## Scope

### In Scope (v1)

- Game model with unique constraint on game name
- Player model (or use Django's built-in User model)
- Rating model tied to a game and a player; each player can only submit one rating per game, but can update it later
- Review model tied to a game and a player
- Game image upload support
- Custom `average_rating` property on the Game model
- REST API endpoints for: creating games, listing/searching games, filtering by category and year, submitting ratings, submitting reviews, uploading images
- Django admin interface for managing data during development

### Out of Scope (future)

- React or other frontend client
- Authentication and authorization (JWT, sessions)
- Social features (following players, comments on reviews)
- External database (PostgreSQL, MySQL)
- Deployment and hosting
- Email notifications
- Pagination and rate limiting

## Success Criteria

- A game cannot be created twice under the same name (enforced at the model/API level)
- The average rating for a game is computed from all submitted ratings and returned by the API without being stored as a database column
- Games can be retrieved filtered by category and by year of release
- Images can be associated with a game via the API
- All endpoints return appropriate HTTP status codes and JSON responses

## Learning Goals

- Build and structure a Django REST Framework project from scratch
- Design related models (Game, Rating, Review, Image) and understand foreign key relationships
- Implement a custom model property in Django
- Write serializers and views for a REST API
- Use Django's ORM for filtering and searching querysets
