<script>
  export let search;
  export let logOut;

  export let height;
</script>

<header bind:clientHeight={height}>
  <h2>Dear Diary</h2>
  
  <section>
    <input id='search' type=text placeholder='Search' bind:value={search}/>
    
    <button on:click={logOut}>
      <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" class="bi bi-box-arrow-left" viewBox="0 0 16 16">
        <path fill-rule="evenodd" d="M6 12.5a.5.5 0 0 0 .5.5h8a.5.5 0 0 0 .5-.5v-9a.5.5 0 0 0-.5-.5h-8a.5.5 0 0 0-.5.5v2a.5.5 0 0 1-1 0v-2A1.5 1.5 0 0 1 6.5 2h8A1.5 1.5 0 0 1 16 3.5v9a1.5 1.5 0 0 1-1.5 1.5h-8A1.5 1.5 0 0 1 5 12.5v-2a.5.5 0 0 1 1 0v2z"/>
        <path fill-rule="evenodd" d="M.146 8.354a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L1.707 7.5H10.5a.5.5 0 0 1 0 1H1.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3z"/>
      </svg>
    </button>
  </section>
</header>

<style>
  header > * {
    padding: 0;
    margin: 0;
  }

  header {
    position: fixed;
    top: 0;

    display: flex;
    align-items: center;
    justify-content: space-around;

    width: 100%;

    background-color: white;

    padding: 5px;
  }

  section {
    display: flex;
    align-items: center;
  }

  #search {
    border: solid 2px #F3F3F3;
    border-radius: 5px;
    
    box-sizing: content-box;
    height: 28px;

    padding-inline: .75rem;
    margin-right: 2vw;
  }

  h2 {
    font-size: 2rem;
    color: var(--accent);
  }

  button {
    border: 0;
    padding: 0;

    background-color: white;

    cursor: pointer;
  }

  svg {
    fill: var(--accent);
  }
</style>