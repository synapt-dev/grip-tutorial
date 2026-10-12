# The demo shop

A tiny shop in five repositories. `demo-core` sets prices, `demo-web` serves
them over HTTP, `demo-api` answers JSON requests, `demo-worker` prices a batch
of orders, and these pages describe them.

- `GET /price?qty=4` returns `{"qty": 4, "cents": 1000}`.
