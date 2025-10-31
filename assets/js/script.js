// Check authentication status on page load
document.addEventListener('DOMContentLoaded', function() {
    const currentPath = window.location.pathname;
    const isLoginPage = currentPath.endsWith('index.html') || currentPath.endsWith('/');
    const isAuthenticated = localStorage.getItem('vtm_user');

    if (isLoginPage && isAuthenticated) {
        window.location.href = 'dashboard.html';
    } else if (!isLoginPage && !isAuthenticated) {
        window.location.href = 'index.html';
    }

    // Initialize login form handler
    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', handleLogin);
    }

    // Initialize dashboard elements
    if (!isLoginPage) {
        initializeDashboard();
    }
});

// Handle login form submission
function handleLogin(e) {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Simple authentication (demo purposes only)
    if (username && password) {
        localStorage.setItem('vtm_user', username);
        window.location.href = 'dashboard.html';
    }
}

// Initialize dashboard functionality
function initializeDashboard() {
    // Display username
    const username = localStorage.getItem('vtm_user');
    document.getElementById('username-display').textContent = username;

    // Sidebar toggle
    document.getElementById('sidebarCollapse').addEventListener('click', function() {
        document.querySelector('.sidebar').classList.toggle('active');
    });

    // Theme toggle
    const themeToggle = document.getElementById('themeToggle');
    const themeIcon = themeToggle.querySelector('i');
    
    themeToggle.addEventListener('click', function() {
        const currentTheme = document.documentElement.getAttribute('data-bs-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        
        document.documentElement.setAttribute('data-bs-theme', newTheme);
        themeIcon.className = newTheme === 'dark' ? 'bi bi-sun-fill' : 'bi bi-moon-fill';
        
        localStorage.setItem('vtm_theme', newTheme);
    });

    // Load saved theme
    const savedTheme = localStorage.getItem('vtm_theme') || 'light';
    document.documentElement.setAttribute('data-bs-theme', savedTheme);
    themeIcon.className = savedTheme === 'dark' ? 'bi bi-sun-fill' : 'bi bi-moon-fill';

    // Handle navigation
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', function(e) {
            if (this.dataset.section) {
                e.preventDefault();
                showSection(this.dataset.section);
            }
        });
    });

    // Logout handler
    document.getElementById('logoutBtn').addEventListener('click', function() {
        localStorage.removeItem('vtm_user');
        window.location.href = 'index.html';
    });
}

// Show selected content section
function showSection(sectionId) {
    // Hide all sections
    document.querySelectorAll('.content-section').forEach(section => {
        section.classList.remove('active');
    });

    // Show selected section
    const targetSection = document.getElementById(`${sectionId}-section`);
    if (targetSection) {
        targetSection.classList.add('active');
    }

    // Update active state in sidebar
    document.querySelectorAll('.nav-link').forEach(link => {
        link.classList.remove('active');
        if (link.dataset.section === sectionId) {
            link.classList.add('active');
        }
    });
}
