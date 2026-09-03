# API Reliability Monitor — SLA Report

> Last updated: **2026-09-03 13:54 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **77.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 70.21% | 3111.4 | 10420.1 | 1000ms | 728/2444 |
| ❌ | `public_apis_list` | 0.0% | 99.43% | 141.4 | 5075.4 | 1500ms | 14/2444 |
| ❌ | `ipapi_check` | 49.18% | 99.96% | 144.9 | 4507.0 | 2500ms | 1/2444 |
| ❌ | `nasa_apod` | 80.65% | 58.67% | 2705.1 | 11152.5 | 2000ms | 1010/2444 |
| ⚠️ | `dog_ceo_random` | 96.89% | 97.59% | 482.9 | 10244.1 | 2500ms | 59/2444 |
| ✅ | `open_meteo_weather` | 99.02% | 98.2% | 675.7 | 14877.1 | 2000ms | 44/2444 |
| ✅ | `rest_countries` | 99.39% | 99.1% | 268.8 | 10221.5 | 2500ms | 22/2444 |
| ✅ | `useless_fact` | 99.67% | 99.67% | 659.0 | 10229.6 | 2500ms | 8/2444 |
| ✅ | `catfact_random` | 99.8% | 99.47% | 261.7 | 10080.2 | 3000ms | 13/2444 |
| ✅ | `coingecko_bitcoin` | 99.84% | 99.92% | 96.5 | 4328.4 | 1500ms | 2/2444 |
| ✅ | `agify_name` | 99.92% | 99.51% | 403.5 | 16112.2 | 2000ms | 12/2444 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.92% | 184.5 | 3882.8 | 2000ms | 2/2444 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4651.1 | 46.15% |
| `numbers_trivia` | 10:00 | 3720.9 | 35.42% |
| `numbers_trivia` | 02:00 | 3519.9 | 33.33% |
| `numbers_trivia` | 00:00 | 3486.1 | 33.33% |
| `numbers_trivia` | 14:00 | 3451.0 | 33.33% |
| `numbers_trivia` | 09:00 | 3334.7 | 32.08% |
| `numbers_trivia` | 17:00 | 3325.2 | 33.07% |
| `nasa_apod` | 03:00 | 3307.4 | 48.08% |
| `nasa_apod` | 17:00 | 3267.7 | 41.27% |
| `nasa_apod` | 05:00 | 3228.7 | 46.48% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
