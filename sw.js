// Offline-Cache für die EVSE-Prüfprotokoll-App
// Online immer frisch vom Server (am Browser-Cache vorbei), offline aus dem eigenen Cache.
const CACHE = "evse-v47";
self.addEventListener("install", e => { e.waitUntil(caches.open(CACHE).then(c => c.addAll([new Request("./", {cache: "reload"}), new Request("./index.html", {cache: "reload"})]))); self.skipWaiting(); });
self.addEventListener("activate", e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k))))); self.clients.claim(); });
self.addEventListener("fetch", e => {
  if (e.request.method !== "GET") return;
  const eigen = new URL(e.request.url).origin === location.origin;
  e.respondWith(fetch(eigen ? new Request(e.request, {cache: "no-cache"}) : e.request).then(r => { const copy = r.clone(); if (eigen && r.ok) caches.open(CACHE).then(c => c.put(e.request, copy)); return r; })
    .catch(() => caches.match(e.request).then(m => m || caches.match("./index.html"))));
});
