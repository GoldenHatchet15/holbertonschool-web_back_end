const updateStudentGradeByCity = (students, city, newGrades) => {
  const gradesMap = newGrades.reduce((acc, { studentId, grade }) => {
    acc[studentId] = grade;
    return acc;
  }, {});

  return students
    .filter((student) => student.location === city)
    .map((student) => ({
      ...student,
      grade: gradesMap[student.id] || 'N/A',
    }));
};

export default updateStudentGradeByCity;
