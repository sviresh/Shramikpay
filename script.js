// ✅ Mobile menu toggle
function toggleMobileMenu() {
  const menu = document.getElementById("mobileMenu");
  menu.classList.toggle("hidden");
}

// ✅ Demo download buttons
function downloadApp(store) {
  if (store === "playstore") {
    alert("📱 Demo only: Play Store link coming soon!");
  } else if (store === "appstore") {
    alert("🍏 Demo only: App Store link coming soon!");
  }
}

// ✅ Pricing toggle
const toggleBtn = document.getElementById("togglePricing");
const pricingCards = document.getElementById("pricingCards");

let yearly = false;
const pricingPlans = {
  monthly: [
    { name: "Basic", price: "₹299", desc: "For small contractors" },
    { name: "Pro", price: "₹499", desc: "For mid-sized projects" },
    { name: "Enterprise", price: "₹799", desc: "For large teams" }
  ],
  yearly: [
    { name: "Basic", price: "₹2,999", desc: "Save 15%" },
    { name: "Pro", price: "₹4,999", desc: "Save 20%" },
    { name: "Enterprise", price: "₹7,999", desc: "Save 25%" }
  ]
};

function renderPricing() {
  const plans = yearly ? pricingPlans.yearly : pricingPlans.monthly;
  pricingCards.innerHTML = plans.map(p => `
    <div class="bg-white rounded-xl shadow-lg p-8 flex flex-col justify-between hover:shadow-xl transition">
      <div>
        <h3 class="text-2xl font-bold text-gray-900 mb-2">${p.name}</h3>
        <p class="text-gray-600 mb-6">${p.desc}</p>
        <div class="text-4xl font-bold text-primary mb-4">${p.price}</div>
      </div>
      <button onclick="alert('Demo activated for ${p.name}!')" class="bg-primary text-white py-3 rounded-lg hover:bg-secondary transition">
        Start Demo
      </button>
    </div>
  `).join('');
}

toggleBtn.addEventListener("click", () => {
  yearly = !yearly;
  toggleBtn.querySelector(".dot").classList.toggle("translate-x-6");
  toggleBtn.classList.toggle("bg-primary");
  renderPricing();
});

renderPricing();

// ✅ Contact form submission (demo only)
document.getElementById("contactForm").addEventListener("submit", function (e) {
  e.preventDefault();
  alert("✅ Thank you! Your message has been sent (demo mode).");
  this.reset();
});
