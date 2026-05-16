# API Reliability Monitor — SLA Report

> Last updated: **2026-05-16 20:25 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 66.92% | 3490.4 | 10206.7 | 1000ms | 264/798 |
| ❌ | `public_apis_list` | 0.0% | 99.5% | 130.8 | 4595.4 | 1500ms | 4/798 |
| ❌ | `nasa_apod` | 76.19% | 56.77% | 3021.2 | 10549.1 | 2000ms | 345/798 |
| ❌ | `ipapi_check` | 84.09% | 100.0% | 154.9 | 363.0 | 2500ms | 0/798 |
| ⚠️ | `rest_countries` | 98.75% | 98.25% | 344.3 | 10221.5 | 2500ms | 14/798 |
| ⚠️ | `open_meteo_weather` | 98.87% | 97.12% | 701.3 | 14877.1 | 2000ms | 23/798 |
| ⚠️ | `dog_ceo_random` | 99.5% | 94.74% | 640.7 | 10244.1 | 2500ms | 42/798 |
| ✅ | `catfact_random` | 99.62% | 99.12% | 270.0 | 10080.2 | 3000ms | 7/798 |
| ✅ | `coingecko_bitcoin` | 99.62% | 100.0% | 98.0 | 252.0 | 1500ms | 0/798 |
| ✅ | `useless_fact` | 99.75% | 99.5% | 606.9 | 10229.6 | 2500ms | 4/798 |
| ✅ | `agify_name` | 99.87% | 99.75% | 390.6 | 16112.2 | 2000ms | 2/798 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.75% | 233.0 | 3882.8 | 2000ms | 2/798 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4729.0 | 77.78% |
| `numbers_trivia` | 03:00 | 4635.3 | 44.44% |
| `numbers_trivia` | 12:00 | 4284.2 | 40.63% |
| `numbers_trivia` | 07:00 | 4196.6 | 40.0% |
| `numbers_trivia` | 05:00 | 4119.9 | 39.13% |
| `nasa_apod` | 17:00 | 4065.2 | 52.17% |
| `numbers_trivia` | 10:00 | 3957.5 | 37.5% |
| `numbers_trivia` | 00:00 | 3937.7 | 37.5% |
| `nasa_apod` | 11:00 | 3814.3 | 43.75% |
| `numbers_trivia` | 14:00 | 3788.5 | 35.71% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
