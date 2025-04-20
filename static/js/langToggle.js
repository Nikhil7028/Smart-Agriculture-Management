
  document.getElementById("lang-toggle-btn").addEventListener("click", function () {
    const currentLang = document.querySelector(".goog-te-combo")?.value || "en";
  const newLang = currentLang === "en" ? "mr" : "en";

  const select = document.querySelector(".goog-te-combo");
  if (select) {
    select.value = newLang;
  select.dispatchEvent(new Event("change"));
  this.innerText = newLang === "en" ? "Marathi" : "English";
    }
  });
  
