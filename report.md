# API Reliability Monitor — SLA Report

> Last updated: **2026-05-13 22:52 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 65.22% | 3647.0 | 10206.7 | 1000ms | 264/759 |
| ❌ | `public_apis_list` | 0.0% | 99.47% | 131.2 | 4595.4 | 1500ms | 4/759 |
| ❌ | `nasa_apod` | 74.97% | 55.73% | 3127.1 | 10549.1 | 2000ms | 336/759 |
| ❌ | `ipapi_check` | 85.11% | 100.0% | 155.2 | 363.0 | 2500ms | 0/759 |
| ⚠️ | `rest_countries` | 98.68% | 98.16% | 351.3 | 10221.5 | 2500ms | 14/759 |
| ⚠️ | `open_meteo_weather` | 98.81% | 96.97% | 709.6 | 14877.1 | 2000ms | 23/759 |
| ⚠️ | `dog_ceo_random` | 99.47% | 94.47% | 654.5 | 10244.1 | 2500ms | 42/759 |
| ✅ | `catfact_random` | 99.6% | 99.08% | 272.6 | 10080.2 | 3000ms | 7/759 |
| ✅ | `coingecko_bitcoin` | 99.6% | 100.0% | 98.2 | 252.0 | 1500ms | 0/759 |
| ✅ | `useless_fact` | 99.74% | 99.47% | 605.1 | 10229.6 | 2500ms | 4/759 |
| ✅ | `agify_name` | 99.87% | 99.74% | 392.2 | 16112.2 | 2000ms | 2/759 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.74% | 234.5 | 3882.8 | 2000ms | 2/759 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4729.0 | 77.78% |
| `numbers_trivia` | 03:00 | 4635.3 | 44.44% |
| `numbers_trivia` | 07:00 | 4535.2 | 43.48% |
| `numbers_trivia` | 12:00 | 4533.3 | 43.33% |
| `nasa_apod` | 17:00 | 4259.2 | 53.49% |
| `numbers_trivia` | 10:00 | 4190.5 | 40.0% |
| `numbers_trivia` | 00:00 | 4168.3 | 40.0% |
| `numbers_trivia` | 05:00 | 4119.9 | 39.13% |
| `nasa_apod` | 11:00 | 3963.6 | 45.65% |
| `numbers_trivia` | 14:00 | 3953.7 | 37.5% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
