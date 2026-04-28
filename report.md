# API Reliability Monitor — SLA Report

> Last updated: **2026-04-28 04:52 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 51.59% | 5035.7 | 10206.7 | 1000ms | 258/533 |
| ❌ | `public_apis_list` | 0.0% | 99.62% | 125.4 | 4088.9 | 1500ms | 2/533 |
| ❌ | `nasa_apod` | 65.67% | 41.65% | 4052.8 | 10549.1 | 2000ms | 311/533 |
| ❌ | `ipapi_check` | 87.99% | 100.0% | 156.3 | 353.0 | 2500ms | 0/533 |
| ⚠️ | `open_meteo_weather` | 98.5% | 97.19% | 723.8 | 14877.1 | 2000ms | 15/533 |
| ⚠️ | `rest_countries` | 98.69% | 98.31% | 340.6 | 10221.5 | 2500ms | 9/533 |
| ⚠️ | `dog_ceo_random` | 99.44% | 92.12% | 767.9 | 10244.1 | 2500ms | 42/533 |
| ✅ | `catfact_random` | 99.44% | 99.44% | 255.5 | 10080.2 | 3000ms | 3/533 |
| ✅ | `useless_fact` | 99.62% | 99.25% | 580.5 | 10229.6 | 2500ms | 4/533 |
| ✅ | `coingecko_bitcoin` | 99.62% | 100.0% | 98.8 | 252.0 | 1500ms | 0/533 |
| ✅ | `agify_name` | 100.0% | 99.81% | 369.9 | 3237.1 | 2000ms | 1/533 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.62% | 239.5 | 3882.8 | 2000ms | 2/533 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6811.3 | 66.67% |
| `numbers_trivia` | 01:00 | 6379.1 | 62.5% |
| `numbers_trivia` | 12:00 | 5840.1 | 56.52% |
| `numbers_trivia` | 18:00 | 5621.4 | 54.17% |
| `numbers_trivia` | 16:00 | 5588.5 | 54.17% |
| `numbers_trivia` | 03:00 | 5523.2 | 53.33% |
| `numbers_trivia` | 07:00 | 5499.9 | 52.94% |
| `nasa_apod` | 03:00 | 5403.4 | 86.67% |
| `numbers_trivia` | 10:00 | 5392.0 | 52.17% |
| `nasa_apod` | 17:00 | 5368.7 | 67.74% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
