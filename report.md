# API Reliability Monitor — SLA Report

> Last updated: **2026-05-13 21:44 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 65.17% | 3651.3 | 10206.7 | 1000ms | 264/758 |
| ❌ | `public_apis_list` | 0.0% | 99.47% | 131.1 | 4595.4 | 1500ms | 4/758 |
| ❌ | `nasa_apod` | 74.93% | 55.67% | 3130.6 | 10549.1 | 2000ms | 336/758 |
| ❌ | `ipapi_check` | 85.09% | 100.0% | 155.2 | 363.0 | 2500ms | 0/758 |
| ⚠️ | `rest_countries` | 98.68% | 98.15% | 351.4 | 10221.5 | 2500ms | 14/758 |
| ⚠️ | `open_meteo_weather` | 98.81% | 96.97% | 709.9 | 14877.1 | 2000ms | 23/758 |
| ⚠️ | `dog_ceo_random` | 99.47% | 94.46% | 655.2 | 10244.1 | 2500ms | 42/758 |
| ✅ | `catfact_random` | 99.6% | 99.08% | 272.8 | 10080.2 | 3000ms | 7/758 |
| ✅ | `coingecko_bitcoin` | 99.6% | 100.0% | 98.3 | 252.0 | 1500ms | 0/758 |
| ✅ | `useless_fact` | 99.74% | 99.47% | 605.2 | 10229.6 | 2500ms | 4/758 |
| ✅ | `agify_name` | 99.87% | 99.74% | 392.2 | 16112.2 | 2000ms | 2/758 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.74% | 234.6 | 3882.8 | 2000ms | 2/758 |

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
