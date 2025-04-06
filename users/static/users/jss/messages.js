document.addEventListener("DOMContentLoaded", function () {
  // Auto-dismiss after 3 seconds
  setTimeout(function () {
    document.querySelectorAll('.alert-box').forEach(function (msg) {
      msg.style.transition = 'opacity 0.5s ease-out';
      msg.style.opacity = '0';
      setTimeout(function () {
        msg.remove();
      }, 500); // Wait for fade-out to finish before removing
    });
  }, 3000);
});