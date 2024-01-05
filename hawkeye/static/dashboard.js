document.addEventListener('DOMContentLoaded', () => {
    const photoUpload = document.getElementById('photo-upload');
    const analyzeButton = document.getElementById('analyze-button');
    const attendanceTable = document.getElementById('attendance-table');
    const pieChartCanvas = document.getElementById('attendance-pie-chart');

    analyzeButton.addEventListener('click', () => {
        const file = photoUpload.files[0];

        if (file) {
            // Perform face recognition and get attendance data here
            // You would typically make an API call to a backend service for this

            // For this example, we'll assume you have a list of student names and attendance status
            const attendanceData = [
                { name: 'Student 1', status: 'Present' },
                { name: 'Student 2', status: 'Absent' },
                { name: 'Student 3', status: 'Present' },
                { name: 'Student 4', status: 'Absent' },
                { name: 'Student 5', status: 'Present' },
                { name: 'Student 6', status: 'Absent' },
                { name: 'Student 7', status: 'Absent' },
                // Add more student data as needed
            ];

            // Calculate the number of students present and absent
            const presentCount = attendanceData.filter(student => student.status === 'Present').length;
            const absentCount = attendanceData.length - presentCount;

            // Update the pie chart data
            updatePieChart(presentCount, absentCount);

            // Generate table rows based on attendance data
            const rows = attendanceData.map((student) => {
                return `
                    <tr>
                        <td>${student.name}</td>
                        <td>${student.status}</td>
                    </tr>
                `;
            });

            // Display the table rows in the attendance table
            attendanceTable.innerHTML = rows.join('');
        } else {
            alert('Please upload a photo before analyzing.');
        }
    });

    function updatePieChart(presentCount, absentCount) {
        const ctx = pieChartCanvas.getContext('2d');
        new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: ['Present', 'Absent'],
                datasets: [{
                    data: [presentCount, absentCount],
                    backgroundColor: ['#36A2EB', '#FF6384'],
                }],
            },
            options: {
                responsive: true,
            },
        });
    }
});
