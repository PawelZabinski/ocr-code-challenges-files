<script>
  import { onMount } from "svelte";
  import Meme from "./lib/Meme.svelte";

  let templates = [];
  let template = null;

  let finishedMeme = null;

  let boxes = [];

  function fillBoxes() {
    boxes = Array(template?.box_count || 0).fill("");
  }

  onMount(async () => {
    const request = await fetch("https://api.imgflip.com/get_memes");
    const json = await request.json();

    templates = json.data.memes;
  });

  function handleClick(newTemplate) {
    template = newTemplate;
    fillBoxes();
  }

  function handleCancel() {
    template = null;
    finishedMeme = null;
    boxes = [];
  }

  async function handleSubmit() {
    const formData = new FormData();

    formData.append("username", "PawelZabinski");
    formData.append("password", "Pawel_17");
    formData.append("template_id", template.id);
    formData.append('font', 'impact');

    boxes.forEach((box, i) => {
      formData.append(`boxes[${i}][text]`, box);
    });

    const response = await fetch("https://api.imgflip.com/caption_image", {
      method: "POST",
      body: formData
    });

    const result = await response.json();

    console.log(result);
    finishedMeme = result.data.url;
  }
</script>

<main>
  {#if !template}
    <h2> Pick a template </h2>

    {#each templates as template (template.id)}
      <Meme { template } { handleClick } />
    {:else}
      <h3> Loading </h3>
    {/each}
  {:else}
    <h2> { template.name } </h2>
    <Meme { template } />

    <form on:submit|preventDefault={handleSubmit}>
      {#each boxes as box, i (i)}
        <input placeholder='Text Box {i + 1}' bind:value={box} />
      {/each}

      <button class='submit-form' type=submit> Build Meme </button>
      <button on:click={handleCancel}> Cancel </button>
    </form>

    {#if finishedMeme}
      <Meme src={finishedMeme} />
    {/if}
  {/if}
</main>

<style>
  :global(body) {
    font-family: Impact, Haettenschweiler, "Arial Narrow Bold", sans-serif;
  }

  main {
    text-align: center;
  }

  form {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  input {
    background-color: #eee;
    border: solid 2px #bbb;
    border-radius: 10px;

    padding: 0.5rem;
  }

  button.submit-form {
    margin-top: 1rem;
  }
</style>