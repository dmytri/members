from playwright.sync_api import expect

def test_login_page(page):
    print("\nTesting login page:")
    
    print("  Navigating to login page")
    page.goto("http://localhost:8000/login")
    
    print("  Checking title")
    expect(page).to_have_title("Login - Members")
    
    print("  Checking form elements")
    expect(page.get_by_label("Email")).to_be_visible()
    expect(page.get_by_label("Password")).to_be_visible()
    expect(page.get_by_role("button", name="Login")).to_be_visible()
    print("  Login page test complete")

def test_register_page(page):
    print("\nTesting register page:")
    
    print("  Navigating to register page")
    page.goto("http://localhost:8000/register")
    
    print("  Checking title")
    expect(page).to_have_title("Register - Members")
    
    print("  Checking form elements")
    expect(page.get_by_label("Email")).to_be_visible()
    expect(page.get_by_label("Password")).to_be_visible()
    expect(page.get_by_role("button", name="Register")).to_be_visible()
    print("  Register page test complete")

def test_registration(client):
    print("\nTesting registration:")
    
    print("  Submitting registration")
    response = client.post('/register', data={
        'email': 'test@example.com',
        'password': 'password123'
    }, follow_redirects=True)
    
    print(f"  Checking response status: {response.status_code}")
    assert response.status_code == 200
    print("  Registration test complete")

def test_login(client):
    print("\nTesting login flow:")
    
    print("  Registering test user")
    client.post('/register', data={
        'email': 'test@example.com',
        'password': 'password123'
    })
    
    print("  Attempting login")
    response = client.post('/login', data={
        'email': 'test@example.com',
        'password': 'password123'
    }, follow_redirects=True)
    
    print(f"  Checking response status: {response.status_code}")
    assert response.status_code == 200
    print("  Login test complete")