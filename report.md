# API Reliability Monitor — SLA Report

> Last updated: **2026-04-26 22:33 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 53.29% | 4869.9 | 10206.7 | 1000ms | 241/516 |
| ❌ | `public_apis_list` | 0.0% | 99.61% | 125.8 | 4088.9 | 1500ms | 2/516 |
| ❌ | `nasa_apod` | 64.53% | 40.31% | 4157.2 | 10549.1 | 2000ms | 308/516 |
| ❌ | `ipapi_check` | 88.95% | 100.0% | 156.7 | 353.0 | 2500ms | 0/516 |
| ⚠️ | `open_meteo_weather` | 98.45% | 97.09% | 729.3 | 14877.1 | 2000ms | 15/516 |
| ⚠️ | `rest_countries` | 98.64% | 98.26% | 344.6 | 10221.5 | 2500ms | 9/516 |
| ⚠️ | `dog_ceo_random` | 99.42% | 91.86% | 781.7 | 10244.1 | 2500ms | 42/516 |
| ✅ | `catfact_random` | 99.42% | 99.42% | 258.6 | 10080.2 | 3000ms | 3/516 |
| ✅ | `useless_fact` | 99.61% | 99.22% | 578.9 | 10229.6 | 2500ms | 4/516 |
| ✅ | `coingecko_bitcoin` | 99.81% | 100.0% | 99.5 | 252.0 | 1500ms | 0/516 |
| ✅ | `agify_name` | 100.0% | 99.81% | 371.2 | 3237.1 | 2000ms | 1/516 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.61% | 240.6 | 3882.8 | 2000ms | 2/516 |

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
