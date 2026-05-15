# API Reliability Monitor — SLA Report

> Last updated: **2026-05-15 16:21 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 66.07% | 3568.6 | 10206.7 | 1000ms | 264/778 |
| ❌ | `public_apis_list` | 0.0% | 99.49% | 131.1 | 4595.4 | 1500ms | 4/778 |
| ❌ | `nasa_apod` | 75.58% | 56.43% | 3071.3 | 10549.1 | 2000ms | 339/778 |
| ❌ | `ipapi_check` | 84.58% | 100.0% | 154.9 | 363.0 | 2500ms | 0/778 |
| ⚠️ | `rest_countries` | 98.71% | 98.2% | 347.4 | 10221.5 | 2500ms | 14/778 |
| ⚠️ | `open_meteo_weather` | 98.84% | 97.04% | 705.4 | 14877.1 | 2000ms | 23/778 |
| ⚠️ | `dog_ceo_random` | 99.49% | 94.6% | 647.9 | 10244.1 | 2500ms | 42/778 |
| ✅ | `catfact_random` | 99.61% | 99.1% | 270.3 | 10080.2 | 3000ms | 7/778 |
| ✅ | `coingecko_bitcoin` | 99.61% | 100.0% | 98.2 | 252.0 | 1500ms | 0/778 |
| ✅ | `useless_fact` | 99.74% | 99.49% | 605.6 | 10229.6 | 2500ms | 4/778 |
| ✅ | `agify_name` | 99.87% | 99.74% | 390.9 | 16112.2 | 2000ms | 2/778 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.74% | 234.4 | 3882.8 | 2000ms | 2/778 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4729.0 | 77.78% |
| `numbers_trivia` | 03:00 | 4635.3 | 44.44% |
| `numbers_trivia` | 12:00 | 4400.0 | 41.94% |
| `numbers_trivia` | 07:00 | 4356.2 | 41.67% |
| `nasa_apod` | 17:00 | 4177.6 | 52.27% |
| `numbers_trivia` | 05:00 | 4119.9 | 39.13% |
| `numbers_trivia` | 10:00 | 4070.5 | 38.71% |
| `numbers_trivia` | 00:00 | 3937.7 | 37.5% |
| `nasa_apod` | 11:00 | 3887.5 | 44.68% |
| `numbers_trivia` | 14:00 | 3873.8 | 36.59% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
