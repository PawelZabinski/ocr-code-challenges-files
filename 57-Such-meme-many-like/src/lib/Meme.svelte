<script>
  export let src = null;
  export let template = null;
  export let handleClick = null;
</script>

<img class='meme' alt={template?.name || 'Meme'} src={src || template?.url} on:click={handleClick && handleClick(template)} />

<style>
  .meme {
    width: 200px;

    border: solid 2px black;
    border-radius: 10px;

    margin: 1rem;
  }
</style>