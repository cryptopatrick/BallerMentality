# BallerMentality Project Build Checklist

---

## Phase 1: Planning & Design
- [ ] Define core features and data models  
  - [ ] Write out core use cases (e.g. login via Google, CRUD on resources, etc.).  
  - [ ] Draft initial data models (users, posts, comments, etc.).
- [ ] Design UI in Figma
  - [ ] Create wireframes or mockups for main views.
  - [ ] Focus on UX for auth flow, dashboard, and key interactions.

---

## Phase 2: Backend Foundations
- [ ] Scaffold Rust project with Poem
- [ ] Set up basic routing and middleware
- [ ] Configure logging and environment management
- [ ] Run PostgreSQL in Docker (manual)
- [ ] Create initial database and user
- [ ] Set up SQLx with DB connection and migrations
- [ ] Implement basic User model
- [ ] Integrate GraphQL with Poem and async-graphql
- [ ] Create test queries and mutations
- [ ] Implement Google OAuth (token exchange, validation, storage)
- [ ] Create login GraphQL mutation

---

## Phase 3: Frontend Foundations
- [ ] Initialize SolidJS project with TypeScript (via Vite or SolidStart)
- [ ] Set up routing, stores, and GraphQL client
- [ ] Implement Google login button (frontend)
- [ ] Handle token exchange and session persistence

---

## Phase 4: Backend API Buildout
- [ ] Expand GraphQL schema with main models (CRUD)
- [ ] Write GraphQL resolvers using SQLx
- [ ] Add authentication guards to schema
- [ ] Write integration tests with Docker PostgreSQL
- [ ] Use sqlx::migrate!() in test setup

---

## Phase 5: Frontend Development
- [ ] Connect frontend to backend via GraphQL
- [ ] Implement core views (dashboard, profile, etc.)
- [ ] Build UI components from Figma
- [ ] Add loading and error states
- [ ] Manage state and caching via signals/stores

---

## Phase 6: Polish & Deployment
- [ ] Handle error responses and input validation
- [ ] Sanitize inputs and secure GraphQL mutations
- [ ] Deploy backend (e.g., Fly.io, Render)
- [ ] Deploy frontend (e.g., Vercel, Netlify)
- [ ] Add CI/CD with GitHub Actions
- [ ] Run type checks, sqlx validation, and build pipelines

---

## Somday
- [ ] Add GitHub authentication fallback
- [ ] Dark mode toggle
- [ ] Offline caching or PWA support