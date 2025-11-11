Origin A loads a script from Origin B using <script src="...">.
- The script is fetched from Origin B but executes in Origin A’s context.
- That means it runs with Origin A’s privileges and can access Origin A resources (DOM, cookies, localStorage, etc.).

But if that script (running under Origin A) tries to **read data** from another domain — for example, Origin B — then:
- **SOP will block** that request.
- To make it work, CORS must be enabled on Origin B’s server to allow Origin A to access its data.

>Note: the script itself can still make requests or exfiltrate data from the page it runs in, so loading untrusted scripts is dangerous.

**SOP = “Domain A script can’t read data from Domain B.”**