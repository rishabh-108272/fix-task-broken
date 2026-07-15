Analyze the Apache-style access log located at '/app/access.log' and generate a JSON summary report at '/app/report.json'.

The JSON report must contain the following keys and values:

1. `total_requests`: The total number of requests in the access log (integer).
2. `unique_ips`: The number of unique client IP addresses (integer).
3. `top_path`: The most frequently requested path (string).
