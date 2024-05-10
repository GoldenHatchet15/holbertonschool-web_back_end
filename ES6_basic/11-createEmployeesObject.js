export default function createEmployeesObject(departmentName, employees) {
  return {
    [departmentName]: employees, // Computed property name
  };
}
