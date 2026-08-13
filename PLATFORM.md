## from platform/main — service topology

The shape of the running system, for anyone who deploys to it:
- web is the storefront; api is the gateway; services stay behind the gateway.
- One direction of dependency: clients call the gateway, never each other.
