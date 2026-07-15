# API Reliability Monitor — SLA Report

> Last updated: **2026-07-15 03:34 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **78.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 81.3% | 2069.2 | 10206.7 | 1000ms | 267/1428 |
| ❌ | `public_apis_list` | 0.0% | 99.72% | 122.3 | 4595.4 | 1500ms | 4/1428 |
| ❌ | `ipapi_check` | 74.3% | 99.93% | 153.7 | 4507.0 | 2500ms | 1/1428 |
| ❌ | `nasa_apod` | 75.63% | 51.4% | 3227.3 | 11152.5 | 2000ms | 694/1428 |
| ❌ | `dog_ceo_random` | 94.89% | 96.57% | 544.4 | 10244.1 | 2500ms | 49/1428 |
| ⚠️ | `open_meteo_weather` | 98.67% | 97.13% | 721.9 | 14877.1 | 2000ms | 41/1428 |
| ⚠️ | `rest_countries` | 98.95% | 98.67% | 309.3 | 10221.5 | 2500ms | 19/1428 |
| ✅ | `useless_fact` | 99.65% | 99.72% | 634.1 | 10229.6 | 2500ms | 4/1428 |
| ✅ | `catfact_random` | 99.79% | 99.37% | 255.9 | 10080.2 | 3000ms | 9/1428 |
| ✅ | `coingecko_bitcoin` | 99.79% | 99.93% | 97.5 | 4328.4 | 1500ms | 1/1428 |
| ✅ | `agify_name` | 99.93% | 99.72% | 385.1 | 16112.2 | 2000ms | 4/1428 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.86% | 208.2 | 3882.8 | 2000ms | 2/1428 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4510.1 | 78.26% |
| `nasa_apod` | 09:00 | 4062.5 | 53.33% |
| `nasa_apod` | 05:00 | 4062.2 | 58.97% |
| `nasa_apod` | 17:00 | 4003.6 | 54.05% |
| `nasa_apod` | 01:00 | 3752.8 | 54.55% |
| `numbers_trivia` | 03:00 | 3681.5 | 34.78% |
| `nasa_apod` | 12:00 | 3605.8 | 53.23% |
| `nasa_apod` | 18:00 | 3577.0 | 50.0% |
| `nasa_apod` | 11:00 | 3539.3 | 51.9% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
