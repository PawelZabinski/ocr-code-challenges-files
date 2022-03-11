<script>
	let value = '';

  const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

  function semaphoreName(char) {
    return `assets/Flag${char.toUpperCase()}.png`;
  }
</script>

<main>
  <h2>Semaphores</h2>
  
  <textarea bind:value placeholder='Enter text' />
  
  <section class='semaphore-translation'>
  	{#each value as char}
      {#if alphabet.includes(char.toUpperCase())}
        <img src={semaphoreName(char)}/>
      {/if}
    {:else}
      <p>Enter some text to see semaphore flags output</p>
    {/each}
  </section>
</main>

<style>
  main {
    width: 100vw;
    min-height: 100vh;

    background: white;

    font-family: Arial;
  }

  textarea {
    border: none;
    border-radius: 10px;

    background: #333;
    color: white;

    font-size: 1rem;
    padding: 1rem;
  }
  
  img {
    width: 100px;
    height: 100px;
  }

  h2 {
    text-align: center;
    font-size: 2rem;

    padding: 1rem;
    margin: 0;
  }

  p {
    color: #888;
  }
</style>