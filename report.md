# API Reliability Monitor — SLA Report

> Last updated: **2026-04-27 15:09 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 52.48% | 4949.4 | 10206.7 | 1000ms | 249/524 |
| ❌ | `public_apis_list` | 0.0% | 99.62% | 125.7 | 4088.9 | 1500ms | 2/524 |
| ❌ | `nasa_apod` | 65.08% | 40.84% | 4109.8 | 10549.1 | 2000ms | 310/524 |
| ❌ | `ipapi_check` | 88.93% | 100.0% | 156.7 | 353.0 | 2500ms | 0/524 |
| ⚠️ | `open_meteo_weather` | 98.47% | 97.14% | 726.6 | 14877.1 | 2000ms | 15/524 |
| ⚠️ | `rest_countries` | 98.66% | 98.28% | 342.3 | 10221.5 | 2500ms | 9/524 |
| ⚠️ | `dog_ceo_random` | 99.43% | 91.98% | 775.7 | 10244.1 | 2500ms | 42/524 |
| ✅ | `catfact_random` | 99.43% | 99.43% | 256.8 | 10080.2 | 3000ms | 3/524 |
| ✅ | `useless_fact` | 99.62% | 99.24% | 580.8 | 10229.6 | 2500ms | 4/524 |
| ✅ | `coingecko_bitcoin` | 99.62% | 100.0% | 99.2 | 252.0 | 1500ms | 0/524 |
| ✅ | `agify_name` | 100.0% | 99.81% | 370.1 | 3237.1 | 2000ms | 1/524 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.62% | 240.6 | 3882.8 | 2000ms | 2/524 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6811.3 | 66.67% |
| `numbers_trivia` | 01:00 | 5854.0 | 57.14% |
| `numbers_trivia` | 12:00 | 5840.1 | 56.52% |
| `numbers_trivia` | 03:00 | 5523.2 | 53.33% |
| `numbers_trivia` | 07:00 | 5499.9 | 52.94% |
| `numbers_trivia` | 18:00 | 5428.6 | 52.17% |
| `nasa_apod` | 03:00 | 5403.4 | 86.67% |
| `numbers_trivia` | 16:00 | 5394.5 | 52.17% |
| `numbers_trivia` | 10:00 | 5392.0 | 52.17% |
| `nasa_apod` | 17:00 | 5368.7 | 67.74% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
