self.addEventListener("install", () => self.skipWaiting());
self.addEventListener("activate", e => e.waitUntil((async () => {
  for (const k of await caches.keys()) if (k === "start-v1" || k === "start-v2") await caches.delete(k);
  await self.registration.unregister();
})()));
