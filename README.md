# CleWe

## Technology stack

* FastAPI
* Postgres 10+

### start project

Pre-requirements: docker and docker-compose should be installed

`make build`


### Useful project links

* swagger - http://localhost/api/swagger/
* redoc - http://localhost/api/redoc/


An application should run on `http://127.0.0.1:8000/`

## UI setup

Prerequisites:

- [ ] Node.js version 18+
- [ ] npm version 8+

1. install `pnpm`

```bash
npm install -g pnpm
```

2. go to `ui` folder from the root of the project

```bash
cd ui
```

3. intall dependencies

```bash
pnpm install
```

4. create and run a production build

```bash
pnpm run build && pnpm start
```

After step #4, the ui should run on `http://localhost:3000/`
