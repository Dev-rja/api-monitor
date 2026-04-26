# API Reliability Monitor — SLA Report

> Last updated: **2026-04-26 15:23 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 54.24% | 4777.7 | 10206.7 | 1000ms | 232/507 |
| ❌ | `public_apis_list` | 0.0% | 99.61% | 126.7 | 4088.9 | 1500ms | 2/507 |
| ❌ | `nasa_apod` | 63.91% | 39.45% | 4219.3 | 10549.1 | 2000ms | 307/507 |
| ❌ | `ipapi_check` | 89.15% | 100.0% | 157.3 | 353.0 | 2500ms | 0/507 |
| ⚠️ | `open_meteo_weather` | 98.42% | 97.24% | 721.0 | 14877.1 | 2000ms | 14/507 |
| ⚠️ | `rest_countries` | 98.62% | 98.22% | 347.2 | 10221.5 | 2500ms | 9/507 |
| ⚠️ | `dog_ceo_random` | 99.41% | 91.72% | 788.9 | 10244.1 | 2500ms | 42/507 |
| ✅ | `catfact_random` | 99.41% | 99.41% | 261.2 | 10080.2 | 3000ms | 3/507 |
| ✅ | `useless_fact` | 99.61% | 99.21% | 580.2 | 10229.6 | 2500ms | 4/507 |
| ✅ | `coingecko_bitcoin` | 99.8% | 100.0% | 100.2 | 252.0 | 1500ms | 0/507 |
| ✅ | `agify_name` | 100.0% | 99.8% | 372.0 | 3237.1 | 2000ms | 1/507 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.61% | 241.5 | 3882.8 | 2000ms | 2/507 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6402.8 | 62.5% |
| `numbers_trivia` | 01:00 | 5854.0 | 57.14% |
| `numbers_trivia` | 12:00 | 5645.9 | 54.55% |
| `nasa_apod` | 17:00 | 5623.1 | 68.97% |
| `nasa_apod` | 03:00 | 5600.9 | 85.71% |
| `nasa_apod` | 18:00 | 5530.3 | 81.82% |
| `numbers_trivia` | 07:00 | 5499.9 | 52.94% |
| `numbers_trivia` | 10:00 | 5392.0 | 52.17% |
| `nasa_apod` | 11:00 | 5354.0 | 63.33% |
| `numbers_trivia` | 18:00 | 5218.5 | 50.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
