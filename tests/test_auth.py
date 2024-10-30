import pytest
from playwright.sync_api import expect

def test_login_page(page):
    # Navigate to login page
    page.goto("http://localhost:8000/login")
    
    # Check title
    expect(page).to_have_title("Login - Members")
    
    # Check form elements
    expect(page.get_by_label("Email")).to_be_visible()
    expect(page.get_by_label("Password")).to_be_visible()
    expect(page.get_by_role("button", name="Login")).to_be_visible()

def test_register_page(page):
    # Navigate to register page
    page.goto("http://localhost:8000/register")
    
    # Check title
    expect(page).to_have_title("Register - Members")
    
    # Check form elements
    expect(page.get_by_label("Email")).to_be_visible()
    expect(page.get_by_label("Password")).to_be_visible()
    expect(page.get_by_role("button", name="Register")).to_be_visible()

def test_successful_registration(page):
    # Navigate to register page
    page.goto("http://localhost:8000/register")
    
    # Fill and submit form
    page.get_by_label("Email").fill("test@example.com")
    page.get_by_label("Password").fill("password123")
    page.get_by_role("button", name="Register").click()
    
    # Should redirect to home
    expect(page).to_have_url("http://localhost:8000/")

def test_successful_login(page):
    # Navigate to login page
    page.goto("http://localhost:8000/login")
    
    # Fill and submit form
    page.get_by_label("Email").fill("test@example.com")
    page.get_by_label("Password").fill("password123")
    page.get_by_role("button", name="Login").click()
    
    # Should redirect to home
    expect(page).to_have_url("http://localhost:8000/") 