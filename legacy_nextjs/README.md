# Python by Example

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Node.js](https://img.shields.io/badge/node-%3E=18.0.0-brightgreen)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)
![Last Commit](https://img.shields.io/github/last-commit/kyungseok-lee/python-by-example)
![Stars](https://img.shields.io/github/stars/kyungseok-lee/python-by-example?style=social)

> A minimalist, multi-language Python example library for hands-on learning.

---

## 📑 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Demo](#-demo)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Environment Variables](#-environment-variables)
- [Testing & Linting](#-testing--linting)
- [Build & Deployment](#-build--deployment)
- [Troubleshooting FAQ](#-troubleshooting-faq)
- [Extensibility & Best Practices](#-extensibility--best-practices)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)
- [Credits](#credits)

---

## 🚀 Overview

**Python by Example** helps you learn Python through practical, annotated examples. Inspired by Go by Example, it features a minimalist UI, multi-language support, and dynamic navigation.

---

## ✨ Features
- 20+ hands-on Python examples with explanations and output
- Multi-language UI (English, Korean, Japanese, Chinese)
- Dynamic routing for each example
- Copy-to-clipboard and "Run in browser" support
- Mobile-first, responsive, SEO-optimized UI
- Modular React components and global state management
- Easily add new examples via JSON

---

## 🖥️ Demo
- [Live Demo](https://python-by-example.vercel.app)
- _Try it now and explore hands-on Python examples!_

---

## 🛠️ Tech Stack
- **Framework:** Next.js 14 (App Router)
- **Language:** TypeScript
- **Styling:** Custom CSS
- **Code Highlighting:** Prism.js
- **State Management:** React Context + useReducer
- **Icons:** Lucide React

---

## 📁 Project Structure
```
src/
├── app/                 # Next.js app router pages
│   ├── example/[slug]/  # Dynamic example pages
│   ├── layout.tsx       # Root layout (providers, meta)
│   ├── page.tsx         # Home page (intro, navigation)
│   └── globals.css      # Global styles
├── components/          # Reusable React components
├── contexts/            # Global state (AppContext, LanguageContext)
├── lib/                 # Utility/data logic (code parsing, data loader)
└── data/                # Static example data (examples.json)
```

---

## ⚡️ Getting Started

### Prerequisites
- Node.js 18+
- npm or yarn

### Installation & Running
```bash
# Clone the repository
$ git clone https://github.com/kyungseok-lee/python-by-example.git
$ cd python-by-example

# Check your Node.js and npm version
$ node -v
$ npm -v

# Install dependencies
$ npm install

# Start the development server
$ npm run dev
```
- Default URL: http://localhost:3000

---

## 🌱 Environment Variables
| Variable                | Description                        | Example                        |
|-------------------------|------------------------------------|--------------------------------|
| NEXT_PUBLIC_API_URL     | (Optional) API endpoint for client | https://api.example.com        |

Create a `.env` file in the project root if you need to override defaults.

---

## 🧪 Testing & Linting

This project is ready for integration with **Jest** (unit tests) and **ESLint/Prettier** (code style/linting).

```bash
# Run unit tests (if implemented)
$ npm run test

# Run linter
$ npm run lint

# Format code
$ npm run format
```

---

## 🏗️ Build & Deployment

### Production Build
```bash
$ npm run build
$ npm start
```

### Deployment
- **Vercel**: [vercel.com](https://vercel.com/) (recommended, zero-config)
- **Netlify**, **AWS**, **Docker**: Supported

#### Example: Docker
```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY . .
RUN npm install && npm run build
EXPOSE 5000
CMD ["npm", "start"]
```

#### Health Check
- Add a health check endpoint at `/api/health` for production monitoring if needed.

---

## ❓ Troubleshooting FAQ

- **npm install fails**
  - Check Node.js version (`node -v` should be 18+)
  - Clear cache: `npm cache clean --force`
  - Remove `node_modules` and `package-lock.json`, then reinstall
- **Port already in use**
  - Change the port in `package.json` or use `PORT=xxxx npm run dev`
- **Other issues**
  - Please open an [issue](https://github.com/kyungseok-lee/python-by-example/issues)

---

## 🔧 Extensibility & Best Practices
- **Multi-language support** via `LanguageContext` and translation dictionaries
- **Dynamic routing** for scalable example addition
- **Global state** with React Context (AppContext, LanguageContext)
- **Static data** for easy content management
- **Modular components** for maintainable UI
- **Accessibility**: ARIA, keyboard navigation (recommended)
- **Testing**: Add Jest/React Testing Library for robust tests
- **CI/CD**: Integrate with GitHub Actions for lint/test/build automation
- **Security**: Use environment variables, sanitize user input

---

## 🤝 Contributing

We welcome all contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

1. Fork the repository and create a new branch (`feature/your-feature`)
2. Develop and test your feature
3. Create a Pull Request (include description and issue number if applicable)
4. Participate in code review and merge

**Code Style & PR Guidelines**
- Use [Conventional Commits](https://www.conventionalcommits.org/)
- Run Prettier and ESLint before submitting PRs
- All PRs are reviewed before merge

---

## 📄 License
- MIT License ([LICENSE](./LICENSE))

---

## 📬 Contact
- Open an issue or submit a PR for questions
- Maintainer: [kyungseok-lee](https://github.com/kyungseok-lee)

---

## Credits
This project is inspired by the design philosophy of [Go by Example](https://gobyexample.com/).