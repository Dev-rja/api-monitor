# API Reliability Monitor — SLA Report

> Last updated: **2026-04-27 11:17 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 52.68% | 4929.6 | 10206.7 | 1000ms | 247/522 |
| ❌ | `public_apis_list` | 0.0% | 99.62% | 125.7 | 4088.9 | 1500ms | 2/522 |
| ❌ | `nasa_apod` | 64.94% | 40.61% | 4123.6 | 10549.1 | 2000ms | 310/522 |
| ❌ | `ipapi_check` | 89.08% | 100.0% | 156.5 | 353.0 | 2500ms | 0/522 |
| ⚠️ | `open_meteo_weather` | 98.47% | 97.13% | 727.5 | 14877.1 | 2000ms | 15/522 |
| ⚠️ | `rest_countries` | 98.66% | 98.28% | 342.9 | 10221.5 | 2500ms | 9/522 |
| ⚠️ | `dog_ceo_random` | 99.43% | 91.95% | 777.1 | 10244.1 | 2500ms | 42/522 |
| ✅ | `catfact_random` | 99.43% | 99.43% | 257.2 | 10080.2 | 3000ms | 3/522 |
| ✅ | `useless_fact` | 99.62% | 99.23% | 578.4 | 10229.6 | 2500ms | 4/522 |
| ✅ | `coingecko_bitcoin` | 99.62% | 100.0% | 99.1 | 252.0 | 1500ms | 0/522 |
| ✅ | `agify_name` | 100.0% | 99.81% | 370.5 | 3237.1 | 2000ms | 1/522 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.62% | 240.7 | 3882.8 | 2000ms | 2/522 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6811.3 | 66.67% |
| `numbers_trivia` | 01:00 | 5854.0 | 57.14% |
| `numbers_trivia` | 12:00 | 5645.9 | 54.55% |
| `numbers_trivia` | 03:00 | 5523.2 | 53.33% |
| `numbers_trivia` | 07:00 | 5499.9 | 52.94% |
| `numbers_trivia` | 18:00 | 5428.6 | 52.17% |
| `nasa_apod` | 03:00 | 5403.4 | 86.67% |
| `numbers_trivia` | 16:00 | 5394.5 | 52.17% |
| `numbers_trivia` | 10:00 | 5392.0 | 52.17% |
| `nasa_apod` | 17:00 | 5368.7 | 67.74% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
