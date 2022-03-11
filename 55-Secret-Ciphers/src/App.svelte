<script>
  import { vigenere, vernan, ceasar } from './lib/utils.js'

  let cipher = 'Ceasar'
  let process = 'Encode'

  const stringKey = 'ocr-code-challenges';
  const intKey = 1;

  let text = '';
  $: newText = encode(cipher, process, text);

  function encode(cipher, process, text) {
    const isEncoding = process == 'Encode';

    if (cipher == 'Vigenere')
      return vigenere(text, stringKey, isEncoding)
    else if (cipher == 'Vernan')
      return vernan(text, stringKey)
    else if (cipher == 'Ceasar')
      return ceasar(text, intKey, isEncoding)
  }

  // Ciphers: Vigenere, Vernan, Ceasar
</script>

<main>
  <h2> Secret Cipher </h2>

  <article>
    <section>
      <label for='ciphers'>Select a Cipher Algoritm:</label>

      <select bind:value={cipher}>
        <option value='Vigenere'>Vigenere</option>
        <option value='Vernan'>Vernan</option>
        <option value='Ceasar'>Ceasar</option>
      </select>
    </section>

    <section>
      <label for='process'>Select a Process:</label>

      <select bind:value={process}>
        <option value='Encode'>Encode</option>
        <option value='Decode'>Decode</option>
      </select>
    </section>
  </article>

  <textarea bind:value={text} />

  <p>{newText}</p>

  <a href="https://mail.google.com/mail/?view=cm&fs=1&su=Can you decrypt this hidden message&body={newText}" target="_blank">Send email</a>
</main>

<footer>
    *string key is "{stringKey}" and integer key is {intKey}
</footer>

<style>
  :global(body) {
    font-family: Helvetica;

    color: var(--primary);

    --width: min(90vw, 300px);
    --height: 150px;

    --accent: #325AA8;
    --primary: black;
    --background: white;

    margin: 0;
    padding: 0;
  }

  main {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

    height: 100vh;
    width: 100vw;
  }

  footer {
    text-align: center;

    color: grey;

    padding: 1rem;
  }

  a {
    padding: .25rem 1rem;

    border: none;
    border-radius: 5px;

    background-color: var(--accent);
    color: var(--background);

    text-decoration: none;
  }

  textarea {
    border-color: var(--accent);
    border-radius: 5px;

    margin-top: 1.5rem;
    padding: 10px;

    width: var(--width);
    height: var(--height);
  }

  section {
    width: var(--width);
  }

  h2 {
    color: var(--accent);
  }

  p {
    border: none;
    border-radius: 5px;

    margin-top: 1.5rem;
    padding: 10px;

    width: var(--width);
    height: var(--height);

    
    background-color: var(--accent);
    color: var(--background);
  }
</style>