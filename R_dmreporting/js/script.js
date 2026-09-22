function toggleSidebar() {
      const sidebar = document.getElementById('sidebar');
      const main = document.getElementById('main-content');
      const buttons = document.querySelectorAll('.menu-t');

      // Toggle collapsed state
      sidebar.classList.toggle('sidebar-collapsed');

      // Toggle width classes
      if (sidebar.classList.contains('sidebar-collapsed')) {
        sidebar.classList.remove('w-40', 'md:w-56');
        sidebar.classList.add('w-16');
        // main.classList.add('ml-16');
        // main.classList.remove('ml-40', 'ml-56');
        buttons.forEach(btn => btn.classList.add('hidden'));
      } else {
        sidebar.classList.add('w-40', 'md:w-56');
        sidebar.classList.remove('w-16');
        // main.classList.remove('ml-16');
        // main.classList.add('ml-40');
        buttons.forEach(btn => btn.classList.remove('hidden'));
      }
    }

function changeboard(showId, hideId, clickedButton) {
    // Switch content
    document.getElementById(showId).style.display = 'block';
    document.getElementById(hideId).style.display = 'none';

    // Update button styles
    const buttons = document.querySelectorAll('.tab-btn');
    buttons.forEach(btn => btn.classList.remove('!bg-gray-700'));

    clickedButton.classList.add('!bg-gray-700');
  }

function changeplatform() {
    const selectedValue = document.getElementById('platform').value;

    // List all possible platforms
    const platforms = ['google', 'facebook', 'instagram', 'linkedin'];

    // Hide all platforms first
    platforms.forEach(id => {
      const div = document.getElementById(id);
      if (div) div.style.display = 'none';
    });

    // Show only the selected platform
    const activeDiv = document.getElementById(selectedValue);
    if (activeDiv) activeDiv.style.display = 'block';
  }

  // Optional: Run once on page load to ensure correct default
  document.addEventListener('DOMContentLoaded', changeplatform);