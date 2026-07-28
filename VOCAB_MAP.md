# Vocabulary Map

The gap that keeps costing points: **I know the thing, but not the textbook word for it.**
Under interview pressure the plain-word version scatters; the formal term signals seniority.

**How to use:** every time I describe something in my own words and there's a "proper" term,
add a row. LEFT = how I actually said it / built it. RIGHT = the word an interviewer expects.
Review this whole doc before every interview.

| What I say / how I built it | The textbook term | One-line why it matters |
|---|---|---|
| Hard-coded report backup if the live one fails | **Deterministic fallback** | Predictable known-good path when the primary fails |
| Status change so only the first writer wins | **Optimistic locking / atomic conditional write** | No lock held; write only if the value is still what I read (compare-and-set) |
| Set the key only if it doesn't already exist | **`SET NX` (Redis) / atomic conditional write** | Distributed-lock primitive; one winner, no race |
| Make sure the same-account jobs run in order | **FIFO group ID (ordering key)** | Serialize a subset while the rest stay parallel |
| Read it, then write it back if unchanged | **Compare-and-swap (CAS)** | Lock-free concurrency; retry on conflict |
| Lock the row so nobody else touches it while I do | **Pessimistic locking** | Hold the lock for the whole transaction; contrast w/ optimistic |
| Don't let a double-click charge twice | **Idempotency (idempotency key)** | Same request twice = same single effect |
| Copy of data kept close to users | **Cache / CDN / replica** (pick by context) | Cut latency + read load off the origin |
| Split the data across machines | **Sharding / horizontal partitioning** | Scale writes + storage past one box |
| Serve stale data for speed, fix it later | **Eventual consistency** | Availability over strict consistency (CAP) |
| A "read" that secretly also writes (hit counter on every visit) | **Write amplification** | Read path becomes write-bound; offload it |
| Send it off and don't wait for the result | **Fire-and-forget (async)** | Redirect user now, count later off the hot path |
| Permanent redirect (cached forever) vs temporary (comes back each time) | **301 vs 302** | 301 kills analytics + edits; 302 keeps them |
| Turn a big number into a short a-zA-Z0-9 string | **Base62 encoding** | 62⁷ ≈ 3.5T short codes in 7 chars |
| Unique ID without a single central counter | **Distributed ID generation (Snowflake / key-range allocation)** | Avoid the counter SPOF/bottleneck |
| Collect N events then write once | **Batching / flush interval / aggregation window** | Flush on count OR time so quiet keys still flush |
| Queue (work items, consumed once) vs stream (replayable log) | **Message queue vs stream (SQS vs Kafka/Kinesis)** | Pick by throughput + replay needs |
| Check cache; on miss read DB then put it back in cache | **Cache-aside (lazy loading)** | Most common cache pattern; next read is a hit |
| One super-popular item overloading its cache node | **Hot key / hot partition** | Sharding won't help (1 key); replicate or app-local cache |
| Copy the same key to many cache nodes to spread reads | **Replication** (vs sharding) | Shard = different keys; replicate = same key, more read capacity |
| Cold cache → everyone hits DB at once | **Thundering herd / cache stampede** | Softens with single-flight + TTL jitter |
| Only the first request loads, others wait for it | **Request coalescing / single-flight** | 1000 misses → 1 DB read |
| Randomize expiry so keys don't all die together | **TTL jitter** | Prevents synchronized stampede |
| Under a network split, stay up vs stay perfectly correct | **AP over CP (CAP theorem)** | Stale redirect > errored redirect for a shortener |

<!-- Add rows as they come up. This doc is never "done." -->
