# Reflection

Student: Dawn Andrei C. Pamesa  Section: TS31

## 1. Which AI recommendation did you modify or reject, and what documentation or execution result justified the decision?

The clearest case was R4. The AI recommended authenticating with an Authorization: Bearer header and predicted 201 Created. I modified both. The local OpenAPI security scheme names an API-key header, X-API-KEY, so a Bearer header is treated as no key at all and would have reproduced the R7 failure by accident. The documented and observed success code for adding a book is 200, not 201. The same pattern repeated in R6 (AI predicted 204, the API returns 200) and R7 (AI predicted 403 for an invalid key, the simulator returns 401). Each correction was settled by the documentation and then confirmed by the status code in Postman, not by argument.

## 2. How do method, path, headers, parameters, payload, and status code work together in a REST request?

Each part answers a different question. The method says what to do (GET reads, POST creates, DELETE removes). The path says which resource: /api/v1/books is the collection and /api/v1/books/{id} is one book. Query parameters shape a read without changing the resource, as includeISBN=true and sortBy=author do in R2. Headers carry metadata about the request: Content-Type tells the server the body is JSON, and X-API-KEY proves the caller is allowed to change data. The payload is the data itself, needed only when creating. The status code is the server's verdict on the whole combination: 200 means it worked, 401 means the authentication part was missing or wrong, 404 means the path pointed at nothing. When a request fails, the status code tells you which of the other parts to inspect first.

## 3. Why should credentials and tokens remain outside AI prompts and submitted evidence?

An AI prompt is sent to a third-party service outside the lab, where it may be logged, retained, or used for training, so a credential pasted there has left the environment it was issued for and cannot be taken back. Submitted evidence is copied, graded and archived by other people, so an unredacted token in a screenshot is as exposed as one posted in public. A token is a credential in its own right: anyone holding it can add or delete books until it expires, without knowing the password. The AI also never needs the value to do its job. It needs the header name and the shape of the request, so a placeholder loses nothing and removes the risk entirely.

## 4. How would rate limits, asynchronous processing, or webhooks affect a larger bulk-book workflow?

The supplied script sends 100 POSTs back to back. Against an API with a rate limit it would start receiving 429 Too Many Requests part way through, and because it raises on any non-200 it would stop with some books added and some not. A larger workflow should pace its requests, read the Retry-After header on a 429, and log which ids succeeded so a rerun resumes instead of duplicating. Asynchronous processing changes what success means: the server would answer 202 Accepted with a job id, and the client would have to poll a status endpoint before treating a book as added. A webhook removes the polling, because the server calls a registered URL when the batch finishes, which suits long imports but needs an endpoint the server can reach and a check that the callback is genuine.

