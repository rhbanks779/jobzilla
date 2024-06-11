// Display Modal
$(document).ready(function () {
  $(".view-job-btn").click(function () {
    var jobTitle = $(this).data("job-title");
    var jobDescription = $(this).data("job-description");
    var jobCompany = $(this).data("job-company");
    var jobLocation = $(this).data("job-location");
    var jobDeadline = $(this).data("job-deadline");

    $("#modalJobTitle").text(jobTitle);
    $("#modalJobDescription").text(jobDescription);
    $("#modalJobCompany").text("Company: " + jobCompany);
    $("#modalJobLocation").text("Location: " + jobLocation);
    $("#modalJobDeadline").text("Application Deadline: " + jobDeadline);
  });
});

// Delete Modal
$(document).ready(function () {
  $("#deleteModal form").submit(function () {
    $("#deleteModal").modal("hide");
  });
});

// Success toast
$(document).ready(function () {
  // Select the toast container element
  var toastContainer = $("#toast-container");

  toastContainer.children(".toast").toast("show");
});
