console.log("sanity check");

const modalInject = val => {
  $("body").append(`
    <div class="ui basic modal deleteModal">
    <div class="ui icon header">
      <i class="exclamation triangle icon"></i>Delete this adventure?
    </div>
    <div class="modal_btn_group">
      <div class="ui teal dismiss button modal_btn"><i class="close icon"></i>Cancel</div>
      <a class="ui delete button modal_btn" href="/delete_post/${val}"><i class="check icon"></i>Delete</a>
    </div>
  </div>
  `);
  $(".deleteModal").modal("show");
};

$("body").on("click", ".delete", event => {
  const postId = parseInt(event.target.id);
  console.log(typeof postId);
  modalInject(postId);
});

$("body").on("click", ".dismiss", () => {
  $(".deleteModal").modal("hide");
  $(".deleteModal").remove();
});
