//——
const deleter = val => {
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
  $(".modal").modal("show");
};

const logout = () => {
  $("body").append(`
    <div class="ui basic modal logoutModal">
      <div class="ui icon header">
        <i class="exclamation triangle icon"></i>Logout?
      </div>
      <div class="modal_btn_group">
        <div class="ui teal dismiss button modal_btn"><i class="close icon"></i>Cancel</div>
        <a class="ui cancel button modal_btn" href="/accounts/logout"><i class="check icon"></i>Confirm</a>
      </div>
    </div>
    `);
  $(".modal").modal("show");
};

//—— Listeners —————————————————————————————//

$("body").on("click", ".delete", event => {
  const postId = parseInt(event.target.id);
  deleter(postId);
});

$("body").on("click", ".logout", () => {
  logout();
});

$("body").on("click", ".dismiss", () => {
  $(".modal").modal("hide");
  $(".modal").remove();
});
