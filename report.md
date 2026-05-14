# API Reliability Monitor — SLA Report

> Last updated: **2026-05-14 21:57 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 65.71% | 3601.1 | 10206.7 | 1000ms | 264/770 |
| ❌ | `public_apis_list` | 0.0% | 99.48% | 131.0 | 4595.4 | 1500ms | 4/770 |
| ❌ | `nasa_apod` | 75.32% | 56.23% | 3091.7 | 10549.1 | 2000ms | 337/770 |
| ❌ | `ipapi_check` | 84.81% | 100.0% | 155.0 | 363.0 | 2500ms | 0/770 |
| ⚠️ | `rest_countries` | 98.7% | 98.18% | 349.1 | 10221.5 | 2500ms | 14/770 |
| ⚠️ | `open_meteo_weather` | 98.83% | 97.01% | 707.3 | 14877.1 | 2000ms | 23/770 |
| ⚠️ | `dog_ceo_random` | 99.48% | 94.55% | 650.6 | 10244.1 | 2500ms | 42/770 |
| ✅ | `catfact_random` | 99.61% | 99.09% | 270.9 | 10080.2 | 3000ms | 7/770 |
| ✅ | `coingecko_bitcoin` | 99.61% | 100.0% | 98.0 | 252.0 | 1500ms | 0/770 |
| ✅ | `useless_fact` | 99.74% | 99.48% | 605.6 | 10229.6 | 2500ms | 4/770 |
| ✅ | `agify_name` | 99.87% | 99.74% | 391.6 | 16112.2 | 2000ms | 2/770 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.74% | 233.7 | 3882.8 | 2000ms | 2/770 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4729.0 | 77.78% |
| `numbers_trivia` | 03:00 | 4635.3 | 44.44% |
| `numbers_trivia` | 07:00 | 4535.2 | 43.48% |
| `numbers_trivia` | 12:00 | 4533.3 | 43.33% |
| `numbers_trivia` | 10:00 | 4190.5 | 40.0% |
| `nasa_apod` | 17:00 | 4177.6 | 52.27% |
| `numbers_trivia` | 00:00 | 4168.3 | 40.0% |
| `numbers_trivia` | 05:00 | 4119.9 | 39.13% |
| `numbers_trivia` | 14:00 | 3953.7 | 37.5% |
| `numbers_trivia` | 16:00 | 3893.1 | 37.14% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
