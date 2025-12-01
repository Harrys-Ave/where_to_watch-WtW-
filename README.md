# where_to_watch-WtW-
Where_to_watch (WtW) is a web application that helps users instantly discover on which streaming platforms a movie or TV series is available across different countries.

---

# Roadmap

## **Phase 1 — Initial Setup**
- Create GitHub repository.
- Initialize a Django project.

---

## **Phase 2 — API Integration**
- Use JustWatch (unofficial) + TMDB (official) combo as APIs + https://www.movieofthenight.com/about/api/pricing
- Create a Django service module to:
  - Search for a title
  - Fetch streaming availability by region
- Add caching (Redis or Django cache) to reduce API calls.

---

## **Phase 3 — Core Functionality**
- Build search form (title + region).
- Build results page containing:
  - Title information
  - Streaming platforms
  - Country availability
  - Direct streaming links

---

## **Phase 4 — Frontend**
- Create a clean interface using **TailwindCSS** or **Bootstrap** or **React**  
  *(Tailwind is recommended as it integrates very well with Django templates).*
- Add autocomplete search (optional).
- Add flags/icons for each region.

---

## **Phase 5 — Deployment**
*(At first the project runs locally: `http://127.0.0.1:8000/`.  
Deployment means hosting it online so it runs at something like `https://where-to-watch.com`.)*

- Deploy using:
  - **Railway** or **Render (free)** → services that host Django apps easily by connecting your GitHub repo.
- Store API keys as environment secrets.
- Enable HTTPS and optionally add a custom domain (`where-to-watch.com`).

---

## **Phase 6 — Extra Features**
- User accounts + saved watchlist.
- Notifications when a title becomes available.
- Compare streaming availability across multiple countries.
