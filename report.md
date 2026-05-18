# API Reliability Monitor — SLA Report

> Last updated: **2026-05-18 12:05 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 67.6% | 3418.7 | 10206.7 | 1000ms | 266/821 |
| ❌ | `public_apis_list` | 0.0% | 99.51% | 130.4 | 4595.4 | 1500ms | 4/821 |
| ❌ | `nasa_apod` | 76.74% | 57.37% | 2974.2 | 10549.1 | 2000ms | 350/821 |
| ❌ | `ipapi_check` | 83.19% | 100.0% | 154.6 | 363.0 | 2500ms | 0/821 |
| ⚠️ | `rest_countries` | 98.78% | 98.29% | 342.5 | 10221.5 | 2500ms | 14/821 |
| ⚠️ | `open_meteo_weather` | 98.9% | 97.08% | 700.4 | 14877.1 | 2000ms | 24/821 |
| ⚠️ | `dog_ceo_random` | 99.39% | 94.88% | 633.5 | 10244.1 | 2500ms | 42/821 |
| ✅ | `catfact_random` | 99.63% | 99.15% | 269.7 | 10080.2 | 3000ms | 7/821 |
| ✅ | `coingecko_bitcoin` | 99.63% | 100.0% | 97.6 | 252.0 | 1500ms | 0/821 |
| ✅ | `useless_fact` | 99.76% | 99.51% | 608.9 | 10229.6 | 2500ms | 4/821 |
| ✅ | `agify_name` | 99.88% | 99.63% | 392.2 | 16112.2 | 2000ms | 3/821 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.76% | 231.6 | 3882.8 | 2000ms | 2/821 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4729.0 | 77.78% |
| `numbers_trivia` | 03:00 | 4635.3 | 44.44% |
| `numbers_trivia` | 05:00 | 4119.9 | 39.13% |
| `numbers_trivia` | 12:00 | 4054.7 | 38.24% |
| `numbers_trivia` | 07:00 | 4051.7 | 38.46% |
| `nasa_apod` | 17:00 | 3990.5 | 51.06% |
| `numbers_trivia` | 10:00 | 3848.7 | 36.36% |
| `nasa_apod` | 11:00 | 3790.7 | 44.9% |
| `numbers_trivia` | 14:00 | 3756.9 | 37.21% |
| `nasa_apod` | 05:00 | 3716.4 | 60.87% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
