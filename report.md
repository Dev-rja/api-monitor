# API Reliability Monitor — SLA Report

> Last updated: **2026-04-26 18:49 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 53.82% | 4819.2 | 10206.7 | 1000ms | 236/511 |
| ❌ | `public_apis_list` | 0.0% | 99.61% | 126.0 | 4088.9 | 1500ms | 2/511 |
| ❌ | `nasa_apod` | 64.19% | 39.73% | 4194.5 | 10549.1 | 2000ms | 308/511 |
| ❌ | `ipapi_check` | 88.85% | 100.0% | 157.1 | 353.0 | 2500ms | 0/511 |
| ⚠️ | `open_meteo_weather` | 98.43% | 97.06% | 730.8 | 14877.1 | 2000ms | 15/511 |
| ⚠️ | `rest_countries` | 98.63% | 98.24% | 345.7 | 10221.5 | 2500ms | 9/511 |
| ⚠️ | `dog_ceo_random` | 99.41% | 91.78% | 785.5 | 10244.1 | 2500ms | 42/511 |
| ✅ | `catfact_random` | 99.41% | 99.41% | 259.9 | 10080.2 | 3000ms | 3/511 |
| ✅ | `useless_fact` | 99.61% | 99.22% | 580.0 | 10229.6 | 2500ms | 4/511 |
| ✅ | `coingecko_bitcoin` | 99.8% | 100.0% | 99.9 | 252.0 | 1500ms | 0/511 |
| ✅ | `agify_name` | 100.0% | 99.8% | 371.1 | 3237.1 | 2000ms | 1/511 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.61% | 240.9 | 3882.8 | 2000ms | 2/511 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6402.8 | 62.5% |
| `numbers_trivia` | 01:00 | 5854.0 | 57.14% |
| `numbers_trivia` | 12:00 | 5645.9 | 54.55% |
| `nasa_apod` | 03:00 | 5600.9 | 85.71% |
| `numbers_trivia` | 07:00 | 5499.9 | 52.94% |
| `numbers_trivia` | 18:00 | 5428.6 | 52.17% |
| `numbers_trivia` | 16:00 | 5394.5 | 52.17% |
| `numbers_trivia` | 10:00 | 5392.0 | 52.17% |
| `nasa_apod` | 17:00 | 5368.7 | 67.74% |
| `nasa_apod` | 11:00 | 5354.0 | 63.33% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
