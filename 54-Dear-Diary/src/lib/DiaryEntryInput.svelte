<script>
  import { createEventDispatcher } from 'svelte';

  const dispatch = createEventDispatcher();

  let value = ''

  function onSubmit() {
    dispatch('publish', {
      content: value
    })

    // Reset value after submit
    value = ''
  }

  // Manage is focused states
  $: isFocused = value.length > 0

</script>

<form on:submit|preventDefault={onSubmit}>
  <textarea class='diary-content' type=text placeholder="What's on your mind?" bind:value />

  <input style='--isFocused: {isFocused ? "visible" : "hidden"}' class='submit' type=submit value='Publish' />
</form>

<style>
  form {
    display: flex;
    flex-direction: column;
    justify-content: left;

    margin-top: max(10vh, 4rem);
  }

  textarea.diary-content {
		background-color: white;

    display: block;

    border: none;
    border-radius: 8px;

    box-shadow: 0 5px 10px rgba(0, 0, 0, 0.12);
			
		width: calc(var(--width) - 2 * 1em);
    height: 3.5em;

    padding: 1em;
    margin-bottom: 1em;

    font-size: .8rem;
  }
  
  input.submit {
    visibility: var(--isFocused);

    margin-right: auto;
    margin-bottom: 1.5rem;
  }
</style>