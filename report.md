# API Reliability Monitor — SLA Report

> Last updated: **2026-05-01 14:21 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 54.84% | 4704.7 | 10206.7 | 1000ms | 261/578 |
| ❌ | `public_apis_list` | 0.0% | 99.65% | 123.2 | 4088.9 | 1500ms | 2/578 |
| ❌ | `nasa_apod` | 68.17% | 45.33% | 3804.7 | 10549.1 | 2000ms | 316/578 |
| ❌ | `ipapi_check` | 87.37% | 100.0% | 156.2 | 353.0 | 2500ms | 0/578 |
| ⚠️ | `rest_countries` | 98.44% | 98.27% | 347.7 | 10221.5 | 2500ms | 10/578 |
| ⚠️ | `open_meteo_weather` | 98.62% | 97.23% | 719.0 | 14877.1 | 2000ms | 16/578 |
| ⚠️ | `dog_ceo_random` | 99.48% | 92.73% | 738.8 | 10244.1 | 2500ms | 42/578 |
| ✅ | `catfact_random` | 99.48% | 99.48% | 250.5 | 10080.2 | 3000ms | 3/578 |
| ✅ | `useless_fact` | 99.65% | 99.31% | 585.0 | 10229.6 | 2500ms | 4/578 |
| ✅ | `coingecko_bitcoin` | 99.65% | 100.0% | 99.0 | 252.0 | 1500ms | 0/578 |
| ✅ | `agify_name` | 100.0% | 99.83% | 369.6 | 3237.1 | 2000ms | 1/578 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.65% | 238.1 | 3882.8 | 2000ms | 2/578 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6148.6 | 60.0% |
| `numbers_trivia` | 03:00 | 5523.2 | 53.33% |
| `nasa_apod` | 03:00 | 5403.4 | 86.67% |
| `numbers_trivia` | 18:00 | 5398.4 | 52.0% |
| `numbers_trivia` | 12:00 | 5382.0 | 52.0% |
| `nasa_apod` | 17:00 | 5367.0 | 66.67% |
| `numbers_trivia` | 07:00 | 5197.7 | 50.0% |
| `numbers_trivia` | 10:00 | 5173.5 | 50.0% |
| `numbers_trivia` | 01:00 | 5126.1 | 50.0% |
| `numbers_trivia` | 16:00 | 4973.9 | 48.15% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
