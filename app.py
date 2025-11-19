# Danh sách để lưu các công việc (dạng dictionary)
tasks = []


def add_task(task_name):
    """Thêm một công việc mới vào danh sách."""
    task = {'name': task_name, 'completed': False}
    tasks.append(task)
    print(f"Đã thêm công việc: '{task_name}'")


def list_tasks():
    """Liệt kê tất cả các công việc hiện có, kèm trạng thái."""
    if not tasks:
        print("Danh sách công việc trống.")
    else:
        print("\nDanh sách công việc hiện có:")
        for i, task in enumerate(tasks, start=1):
            status = "[x]" if task['completed'] else "[ ]"
            print(f"{i}. {status} {task['name']}")


def complete_task(task_index):
    """Đánh dấu công việc là hoàn thành."""
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        print(f"✅ Đã hoàn thành công việc: '{tasks[task_index]['name']}'")
    else:
        print("❌ Không tìm thấy công việc với chỉ số đã nhập.")


def delete_task(task_index):
    """Xóa một công việc khỏi danh sách."""
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f"🗑️ Đã xóa công việc: '{removed_task['name']}'")
    else:
        print("❌ Không thể xóa: chỉ số công việc không hợp lệ.")


# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")

    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")
    list_tasks()

    # Đánh dấu công việc thứ nhất hoàn thành
    complete_task(0)

    # Xóa công việc thứ hai
    delete_task(1)

    list_tasks()
