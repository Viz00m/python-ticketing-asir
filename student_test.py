
import sys
import os

# Add the current directory to sys.path so we can import backend modules
sys.path.append(os.getcwd())

from backend.logic import auth_manager, ticket_engine, assignment_logic

def print_result(test_name, success, message=""):
    status = "[✓] PASSED" if success else "[X] FAILED"
    print(f"{status} - {test_name}")
    if message:
        print(f"    -> {message}")

def test_logic():
    print("=== Testing Student Implementation ===")
    
    # 1. Test Login
    print("\n--- Testing Auth Manager ---")
    try:
        # Assuming admin/password exists from seed
        result = auth_manager.login("admin", "password")
        if result:
            print_result("Login with valid credentials", True, str(result))
        else:
            print_result("Login with valid credentials", False, "Returned None or empty")
    except NotImplementedError:
        print_result("Login with valid credentials", False, "Not Implemented yet")
    except Exception as e:
        print_result("Login with valid credentials", False, f"Error: {e}")

    # 2. Test Create Ticket
    print("\n--- Testing Ticket Engine (Create) ---")
    ticket_data = {
        "title": "Test Ticket from Script",
        "description": "This is a test ticket created via student_test.py",
        "priority": "medium"
    }
    created_ticket_id = None
    try:
        new_ticket = ticket_engine.create_ticket(ticket_data)
        if new_ticket and "id" in new_ticket:
            created_ticket_id = new_ticket["id"]
            print_result("Create Ticket", True, f"Created ID: {created_ticket_id}")
        else:
            print_result("Create Ticket", False, "Returned invalid data")
    except NotImplementedError:
        print_result("Create Ticket", False, "Not Implemented yet")
    except Exception as e:
        print_result("Create Ticket", False, f"Error: {e}")

    # 3. Test Assign Logic (only if ticket created, or simulate validation)
    print("\n--- Testing Assignment Logic ---")
    # For testing, we might try to assign ticket ID 1 if creation failed
    test_id = created_ticket_id if created_ticket_id else 1 
    
    try:
        result = assignment_logic.smart_assign(test_id)
        print_result(f"Smart Assign Ticket {test_id}", True, str(result))
    except NotImplementedError:
        print_result(f"Smart Assign Ticket {test_id}", False, "Not Implemented yet")
    except Exception as e:
        print_result(f"Smart Assign Ticket {test_id}", False, f"Error: {e}")

    # 4. Test Resolve Logic
    print("\n--- Testing Ticket Engine (Resolve) ---")
    try:
        result = ticket_engine.resolve_ticket(test_id, "Fixed via test script")
        print_result(f"Resolve Ticket {test_id}", True, str(result))
    except NotImplementedError:
        print_result(f"Resolve Ticket {test_id}", False, "Not Implemented yet")
    except Exception as e:
        print_result(f"Resolve Ticket {test_id}", False, f"Error: {e}")

if __name__ == "__main__":
    test_logic()
