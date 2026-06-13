# Recipe Finder 

A web app where you can discover, save, and manage recipes — built with Django.

Whether you're looking for something quick on a weeknight or want to explore cuisines from around the world, Recipe Finder helps you find what you're craving. Users can browse recipes, filter by category or dietary preference, save favorites, and see what's trending. Staff members also get a full admin dashboard to manage content and users.

---

## What it can do

**For visitors & logged-in users:**
- Browse recipes on the homepage — newest dishes up front, classics further down
- Filter by category (Breakfast, Dinner, Desserts, etc.) or dietary tags like vegan, gluten-free, dairy-free
- Search across recipe names, descriptions, and ingredients at the same time
- Click into any recipe for the full breakdown: ingredients, steps, prep/cook time, servings, difficulty
- Save recipes to your personal favorites list
- Check the Trending page to see what other people are loving right now
- Create and edit your own profile (update username, email, or password)

**For staff / admins:**
- A dedicated dashboard showing site stats: total users, active accounts, recipes, and recent activity
- Full recipe management — add new ones, edit existing ones, delete old ones
- User management — search users, toggle staff permissions, deactivate or delete accounts
- An activity log so nothing sneaks past you

---

## Tech stack

| Layer | What's used |
|---|---|
| Framework | Django 6.0.5 |
| Language | Python |
| Database | SQLite3 |
| Image handling | Pillow |
| Frontend | HTML, CSS, vanilla JS (Web Components for navbar & footer) |

No React, no heavy frontend framework — just clean templates and a bit of JavaScript where it counts.

---

## Project structure

```
WEB/
├── config/          # Django settings, root URLs, WSGI/ASGI
├── accounts/        # Signup, login, logout, user profiles
├── recipes/         # The core of the app — browsing, searching, recipe detail
├── social/          # Favorites and trending
├── management/      # Staff-only admin dashboard
├── templates/       # Global base template (navbar + footer live here)
├── static/          # CSS, JS, and images
└── media/           # User-uploaded recipe photos
```

Each feature lives in its own Django app, so things stay organized and don't step on each other.

---

## Getting started

**1. Clone the repo and set up a virtual environment**

```bash
git clone <your-repo-url>
cd WEB
python -m venv .venv
```

**2. Activate the virtual environment**

On Windows:
```bash
.venv\Scripts\activate
```

On Mac/Linux:
```bash
source .venv/bin/activate
```

**3. Install dependencies**

```bash
pip install django pillow
```

**4. Set up the database**

```bash
python manage.py migrate
```

**5. Create an admin account**

```bash
python manage.py createsuperuser
```

**6. Run the development server**

```bash
python manage.py runserver
```

Then open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser and you're in.

---

## Pages at a glance

| URL | What's there |
|---|---|
| `/` | Homepage with featured and classic recipes |
| `/recipes/` | Full recipe list |
| `/recipes/<category>/` | Recipes filtered by category |
| `/recipe/<id>/` | Individual recipe page |
| `/search/?q=...` | Search results |
| `/accounts/signup/` | Create an account |
| `/accounts/login/` | Log in |
| `/accounts/profile/` | Your profile |
| `/social/favorites/` | Your saved recipes |
| `/social/trending/` | Top 10 most-favorited recipes |
| `/management/dashboard/` | Staff dashboard (staff only) |

---

## A few things worth knowing

- **Login works with email or username** — either one gets you in
- **Favorites are per-user** — each account has their own saved list
- **Trending is calculated live** — it counts how many users have favorited each recipe
- **The admin dashboard is staff-only** — regular users can't access it even if they find the URL
- **Recipe images are optional** — recipes without photos still look fine


