<script>
  export let diary;
</script>

<article>
  <section>
    <h3>{diary.author}</h3>
    <h5>{diary.timestamp.toLocaleDateString()}</h5>
  </section>

  <p>{diary.content}</p>
</article>

<style>
  article {
    border: 1px solid #eaeaea;
    border-radius: 8px;
    margin-bottom: 16px;
    background-color: white;
    transition: 0.15s box-shadow ease-in-out;

    padding-inline: 1em;
    width: calc(var(--width) - 2 * 1em);
  }

  section {
    display: flex;
    justify-content: space-between;
  }

  p {
    text-align: left;
  }
</style>